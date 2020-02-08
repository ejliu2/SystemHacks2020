const express = require('express');
const path = require('path');
const { spawn } = require('child_process');
const PORT = process.env.PORT || 5000
const PythonShell = require('python-shell');
var app = express();

app.use(express.static(path.join(__dirname, '/public/')))
app.use(express.json())
app.use(express.urlencoded({ extended:false }))
app.set('views', path.join(__dirname, 'public'))
app.set('view engine', 'ejs')
app.listen(PORT, () => console.log(`Listening on ${ PORT }`))

app.get('/', (req, res) => {
    res.render('sh.ejs')
});

app.post("/submit", (req, res) => {
    var result = spawn('python3', ["-u", path.join(__dirname, 'craigslist_scraper.py'), req.body.searchProduct]);

    result.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });

    result.stderr.on('data', (data) => {
        console.log(`stderr: ${data}`);
    });

    result.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
    });

    res.render('results.ejs')
});