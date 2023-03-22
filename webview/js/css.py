src = """
(function() {
    var loadCss = setInterval(function() {
        if (document.readyState === "complete") {
            clearInterval(loadCss);
            
            var css = document.createElement("style");
            css.type = "text/css";
            css.innerHTML = "%s";
            document.head.appendChild(css);
        }
    }, 10);    
})()
"""