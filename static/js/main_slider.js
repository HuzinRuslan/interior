class Slider {
    constructor(){
        this.currentIdx = 1;
        this.maxIdx = 2;
        this.container = document.querySelector('.slider')
        this.slides = document.querySelectorAll('.slide')
        this.icons = document.querySelectorAll('.icon')
        this._init()
    }

    _init(){
        this._clickHandlers()
        this._showImageWithCurrentIdx();
        this._makeInterval();
    }

    _clickHandlers(){
        this.icons.forEach(icon => {icon.addEventListener('click', ()=> {
            this._refreshIcons();
            this._changeImage();
            this.currentIdx = icon.dataset.id;
            icon.classList.add('icon-active');
        })})
    }
    
    _refreshIcons(){
        this.icons.forEach(icon => {icon.classList.remove('icon-active')})
    }

    _showImageWithCurrentIdx(){
        this.slides[this.currentIdx].classList.remove('hidden')
    }

    _hideVisibleImage(){
        this.slides[this.currentIdx].style.animation = '';
        document.querySelector('.slide:not(.hidden)').classList.add('hidden');
    }

    _changeImage() {
        this.slides[this.currentIdx].style.animation = 'fade-out 0.3s ease-in-out';
        setTimeout(() => {
            this._hideVisibleImage();
            this._showImageWithCurrentIdx();
        }, 300);
    }
    
    _makeInterval(){
        setInterval(this.intervalFunc.bind(this) , 4000)
    }

    intervalFunc(){
        if (this.currentIdx == this.maxIdx){
            this.icons[0].click()
        }
        else{
            this.icons[Number(this.currentIdx) + 1].click()
        }
    }
}

s = new Slider()