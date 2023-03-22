src = """
window.alert = function(message) {
    windows.external.alert(message);
}
"""