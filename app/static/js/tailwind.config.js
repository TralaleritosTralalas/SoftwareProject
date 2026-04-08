tailwind.config = {
    darkMode: "class",
    theme: {
        extend: {
            colors: {
                "primary": "#256af4",
                "background-light": "#f5f6f8",
                "background-dark": "#101622",
                "surface-dark": "#182234",
                "surface-light": "#ffffff",
                "border-dark": "#222f49",
                "border-light": "#e2e8f0",
            },
            fontFamily: {
                "display": ["Spline Sans", "sans-serif"]
            },
            borderRadius: {
                "DEFAULT": "0.25rem", 
                "lg": "0.5rem", 
                "xl": "0.75rem", 
                "full": "9999px"
            },
        },
    },
}