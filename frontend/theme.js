// Create theme toggle UI and handle toggling
document.addEventListener('DOMContentLoaded', () => {
    // Create the Navbar
    const navbar = document.createElement('div');
    navbar.className = 'navbar';
    
    // Create Branding
    const brand = document.createElement('h1');
    brand.className = 'brand';
    brand.innerText = 'IntelliHire-ai';
    navbar.appendChild(brand);

    // Inject the theme switch UI into the navbar
    const themeWrapper = document.createElement('div');
    themeWrapper.className = 'theme-switch-wrapper';
    
    // Create text label
    const themeLabel = document.createElement('span');
    themeLabel.innerText = 'Dark Mode';
    themeLabel.style.fontSize = '14px';
    themeLabel.style.fontWeight = 'bold';
    themeWrapper.appendChild(themeLabel);
    
    // Create label and input
    const label = document.createElement('label');
    label.className = 'theme-switch';
    label.setAttribute('for', 'checkbox');
    
    const input = document.createElement('input');
    input.type = 'checkbox';
    input.id = 'checkbox';
    
    const slider = document.createElement('div');
    slider.className = 'slider round';
    
    label.appendChild(input);
    label.appendChild(slider);
    themeWrapper.appendChild(label);
    
    navbar.appendChild(themeWrapper);
    
    document.body.insertBefore(navbar, document.body.firstChild);

    const currentTheme = localStorage.getItem('theme');
    
    if (currentTheme) {
        document.documentElement.setAttribute('data-theme', currentTheme);
        if (currentTheme === 'dark') {
            input.checked = true;
        }
    } else {
        const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)').matches;
        if (prefersDarkScheme) {
            document.documentElement.setAttribute('data-theme', 'dark');
            input.checked = true;
        }
    }

    input.addEventListener('change', function(e) {
        if (e.target.checked) {
            document.documentElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
        }
        else {
            document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
        }    
    });
});
