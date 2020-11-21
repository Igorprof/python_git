'use strict';

const gallery = {
    settings: {
        previewSelector: '.mySuperGallery',
        openedImageWrapperClass: 'galleryWrapper',
        openedImageClass: 'galleryWrapper__image',
        openedImageScreenClass: 'galleryWrapper__screen',
        openedImageCloseBtnClass: 'galleryWrapper__close',
        openedImageCloseBtnSrc: 'images/gallery/close.png',
        openedImageNextBtnClass: 'galleryWrapper__nextBtn',
        openedImageNextBtnSrc: 'images/gallery/next.png',
        openedImagePrevBtnClass: 'galleryWrapper__prevBtn',
        openedImagePrevBtnSrc: 'images/gallery/prev.png',
    },

    screenCotainer: null,

    init(userSettings = {}) {
        Object.assign(this.settings, userSettings);

        document.querySelector(this.settings.previewSelector)
            .addEventListener('click', (event) => {
                this.containerClickHandler(event);
            });
    },

    containerClickHandler(event) {
        if (event.target.tagName !== 'IMG') return;

        this.openImage(event.target.dataset.full_image_url);
    },

    openImage(src) {
        this.screenCotainer = this.getScreenContainer();
        const image = this.screenCotainer.querySelector(`.${this.settings.openedImageClass}`);
        image.addEventListener('error', () => {
            alert('Картинки не существует');
            // this.close();
        });
        image.src = src;
    },

    getScreenContainer() {
        const galleryWrapperElement = document
            .querySelector(`.${this.settings.openedImageWrapperClass}`);

        if (galleryWrapperElement) return galleryWrapperElement;

        return this.createScreenContainer();
    },

    createScreenContainer() {
        const galleryWrapperElement = document.createElement('div');
        galleryWrapperElement.classList.add(this.settings.openedImageWrapperClass);

        const galleryScreenElement = document.createElement('div');
        galleryScreenElement.classList.add(this.settings.openedImageScreenClass);
        galleryWrapperElement.appendChild(galleryScreenElement);

        const closeImageElement = new Image();
        closeImageElement.classList.add(this.settings.openedImageCloseBtnClass);
        closeImageElement.src = this.settings.openedImageCloseBtnSrc;
        closeImageElement.addEventListener('click', () => this.close());
        galleryWrapperElement.appendChild(closeImageElement);

        const image = new Image();
        image.classList.add(this.settings.openedImageClass);
        galleryWrapperElement.appendChild(image);

        const nextBtnElement = new Image();
        nextBtnElement.classList.add(this.settings.openedImageNextBtnClass);
        nextBtnElement.src = this.settings.openedImageNextBtnSrc;
        nextBtnElement.addEventListener('click', () => this.nextImage());
        galleryWrapperElement.appendChild(nextBtnElement);

        const prevBtnElement = new Image();
        prevBtnElement.classList.add(this.settings.openedImagePrevBtnClass);
        prevBtnElement.src = this.settings.openedImagePrevBtnSrc;
        prevBtnElement.addEventListener('click', () => this.prevImage());
        galleryWrapperElement.appendChild(prevBtnElement);

        document.body.appendChild(galleryWrapperElement);

        return galleryWrapperElement;
    },

    nextImage() {
        const image = this.screenCotainer.querySelector(`.${this.settings.openedImageClass}`);
        const newSrc = image.src.slice(0, image.src.lastIndexOf('/') + 1) + (parseInt(image.src.slice(image.src.lastIndexOf('/') + 1, image.src.lastIndexOf('.'))) + 1) + '.jpg';
        image.src = newSrc;
    },

    prevImage() {
        const image = this.screenCotainer.querySelector(`.${this.settings.openedImageClass}`);
        const newSrc = image.src.slice(0, image.src.lastIndexOf('/') + 1) + (parseInt(image.src.slice(image.src.lastIndexOf('/') + 1, image.src.lastIndexOf('.'))) - 1) + '.jpg';
        image.src = newSrc;
    },

    close() {
        document.querySelector(`.${this.settings.openedImageWrapperClass}`).remove();
        this.screenCotainer = null;
    },
};

gallery.init({previewSelector: '.galleryPreviewsContainer'})
