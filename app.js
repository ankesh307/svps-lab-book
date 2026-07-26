document.addEventListener('DOMContentLoaded', () => {
    // Views
    const viewTracks = document.getElementById('view-tracks');
    const viewTiers = document.getElementById('view-tiers');
    const viewCurriculum = document.getElementById('view-curriculum');

    // Buttons / Cards
    const trackCards = document.querySelectorAll('.track-card');
    const tierCards = document.querySelectorAll('.tier-card');
    const backToTracksBtn = document.getElementById('back-to-tracks');
    const backToTiersBtn = document.getElementById('back-to-tiers');

    // Content areas
    const currTitle = document.getElementById('curr-title');
    const currKitInfo = document.getElementById('curr-kit-info');
    const currContent = document.getElementById('curriculum-content');

    let currentTrack = null;

    // Navigation logic
    function showView(viewToShow) {
        [viewTracks, viewTiers, viewCurriculum].forEach(view => {
            view.classList.remove('active');
            view.classList.add('hidden');
        });
        viewToShow.classList.remove('hidden');
        viewToShow.classList.add('active');
    }

    // Track Selection
    trackCards.forEach(card => {
        card.addEventListener('click', () => {
            currentTrack = card.getAttribute('data-track');
            showView(viewTiers);
        });
    });

    // Tier Selection
    tierCards.forEach(card => {
        card.addEventListener('click', () => {
            const currentTier = card.getAttribute('data-tier');
            renderCurriculum(currentTrack, currentTier);
            showView(viewCurriculum);
        });
    });

    // Back Buttons
    backToTracksBtn.addEventListener('click', () => {
        currentTrack = null;
        showView(viewTracks);
    });

    backToTiersBtn.addEventListener('click', () => {
        showView(viewTiers);
    });

    // Render logic
    function renderCurriculum(track, tier) {
        const data = curriculumData[track][tier];
        
        currTitle.textContent = data.title;
        currKitInfo.innerHTML = `<strong>Kit Requirements:</strong> ${data.kit}`;
        
        currContent.innerHTML = ''; // Clear previous content

        data.modules.forEach(module => {
            const modSection = document.createElement('div');
            modSection.className = 'module-section';
            
            const modTitle = document.createElement('h3');
            modTitle.className = 'module-title';
            modTitle.textContent = module.title;
            // Add specific color based on track for extra polish
            if(track === 'robotics-hardware') {
                modTitle.style.color = 'var(--accent-robotics)';
            } else {
                modTitle.style.color = 'var(--accent-ai)';
            }
            
            const dayList = document.createElement('ul');
            dayList.className = 'day-list';
            
            module.days.forEach(day => {
                const li = document.createElement('li');
                li.className = 'day-item';
                
                const typeClass = day.type.toLowerCase() === 'fundamental' ? 'type-fundamental' : 
                                  day.type.toLowerCase() === 'project' ? 'type-project' : 'type-test';
                
                li.innerHTML = `
                    <div class="day-number">Day ${day.day}</div>
                    <div class="day-type ${typeClass}">${day.type}</div>
                    <div class="day-content">
                        <div class="day-title">${day.title}</div>
                        <div class="day-desc">${day.desc}</div>
                    </div>
                `;
                dayList.appendChild(li);
            });
            
            modSection.appendChild(modTitle);
            modSection.appendChild(dayList);
            currContent.appendChild(modSection);
        });
    }
});
