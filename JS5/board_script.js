const board = {   
    rows: 9,
    cols: 9, 
    cellSize: 75, 
    letters: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    boardElement: null,
    cells: null,
    setCellSize(size) {
        this.cellSize = size;
    },
    createCell() {
        const td = document.createElement('td');     
        td.style.textAlign = 'center'; 
        td.style.border = '1px black solid';
        td.style.height = this.cellSize + 'px';
        td.style.width = this.cellSize + 'px';
        return td;
    }, 
    generateBoard() {
        this.boardElement = document.getElementById('board');
        this.cells = [];
        for (let i = 0; i < this.rows; i++) {
            const tr = document.createElement('tr');
            this.boardElement.appendChild(tr);
            const cellsRow = [];
            for (let j = 0; j < this.cols; j++) {
                const td = this.createCell();   
                let isPlayCell = true;

                if (j == 0) {
                    td.style.width = Math.floor(this.cellSize / 3) + 'px';
                    if (i < this.rows - 1) {               
                        td.innerText = String(this.rows - 1 - i);
                    }      
                    isPlayCell = false;           
                } 

                if (i == this.rows - 1) {
                    td.style.height = Math.floor(this.cellSize / 3) + 'px';
                    if (j > 0) {
                        td.innerText = this.letters[j - 1];
                    }
                    isPlayCell = false;
                }
                if (isPlayCell && ((i + j) % 2 == 0)) {
                    td.style.color = 'white';
                    td.style.backgroundColor = 'black';
                }
                tr.appendChild(td);
                if (isPlayCell) {
                    cellsRow.push(td);
                }                
            }
            if (cellsRow.length) {
                this.cells.push(cellsRow);
            }            
        }
    },
    addFigures() {
        if (!this.cells) {
            console.log('Сначала необходимо сгенерировать доску.');
            return;
        }
        for (let i = 0; i < this.rows - 1; i++) {
            for (let j = 0; j < this.cols - 1; j++) {                    
                this.cells[i][j].innerText = this.figureCoords(i, j);
            }
        }
    },
    figureCoords(i, j) {
        if ((i > 1) && (i < 6)) {
            return '';
        }
        if ((i == 1) || (i == 6)) {
            return 'П';
        }
        if ((j == 0) || (j == 7)) {
            return 'Л';
        }
        if ((j == 1) || (j == 6)) {
            return 'Кн';
        }
        if ((j == 2) || (j == 5)) {
            return 'С';
        }
        if (j == 3) {
            return 'Ф';
        }
        if (j == 4) {
            return 'K';
        }
    }
}

board.setCellSize(80);
board.generateBoard();
board.addFigures();

