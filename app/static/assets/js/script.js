const menuPrincipalLink = document.querySelectorAll('.li-link')

menuPrincipalLink.forEach(link => {
    link.addEventListener('click', () => {
        window.open(link.children[0].href, '_self')
    })
})