const settings = {
    rowCount: 10,
    colCount: 10,
    startPositionX: 4,
    startPositionY: 4
}

const player = {
    x: null,
    y: null,

    init(startX, startY) {
        this.x = startX;
        this.y = startY;
    },
    move(direction) {
        switch (direction) {
            case 2:
                this.y++;
                break;
            case 4:
                this.x--;
                break;
            case 6:
                this.x++;
                break;
            case 8:
                this.y--;
                break;
        }
    }
}

const game = {
    settings,
    player,

    run() {
        this.player.init(this.settings.startPositionX, this.settings.startPositionY);

        while (true) {
            this.render();

            const direction = this.getDirection();

            if (direction === -1) {               
                return alert('до свидания!');;
            }
            if ((this.player.x === 0 && direction === 4) || 
            (this.player.x === this.settings.colCount - 1 && direction === 6) || 
            (this.player.y === 0 && direction === 8) || 
            (this.player.y === this.settings.rowCount - 1 && direction === 2)) {
                alert('Выход за пределы на карты!');
            } else {
                this.player.move(direction);
            }           

        }
    }, 
    

    render() {
        let map = '';
        for (let row = 0; row < this.settings.rowCount; row++) {
            for (let col = 0; col < this.settings.colCount; col++) {
                if (this.player.y === row && this.player.x === col) {
                    map += '0 ';
                } else {
                    map += 'X ';
                }
            }
            map += '\n';
        }
        console.clear();
        console.log(map);
    }, 

    getDirection() {
        const avaiDirs = [-1, 2, 4, 6, 8];

        while (true) {
            const d = parseInt(prompt('Введите направление'));

            if (!avaiDirs.includes(d)) {
                alert('некорректный ввод');
                continue;
            }

            return d;
        }
    }
}

game.run();