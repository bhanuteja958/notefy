let editorForm = document.querySelector('.editor__form');
let titleInput = document.querySelector('.editor__titleInput');
let markdownInput = document.querySelector('.editor__markdownInput');
let titleContent = document.querySelector('.note__title');
let noteContent = document.querySelector('.note__content');

let editBtn = document.querySelector('.editor__editBtn');
let saveBtn = document.querySelector('.editor__saveBtn');
let closeBtn = document.querySelector('.editor__closeIcon');

let noteForm = document.querySelector('.editor__formInputs');

let converter = new showdown.Converter();


titleInput.addEventListener('keyup', (e) => {
    const { value } = e.target;
    
    titleContent.style.color = (value === "") ? '#CCCCCC' : '#000000';
    titleContent.textContent = (value === "") ? 'Title will appear here' : value; 
});

markdownInput.addEventListener('keyup', (e) => {
    const { value } = e.target;

    let htmlOutput = converter.makeHtml(value);
    console.log(htmlOutput);
    noteContent.innerHTML = (value === "") ? 'Content will appear here' :  htmlOutput;
})


editBtn.addEventListener('click', () => {
    saveBtn.style.display = "inline";
    editBtn.style.display = "none";

    editorForm.style.display = "grid";
});

closeBtn.addEventListener("click", () => {
    saveBtn.style.display = "none";
    editBtn.style.display = "inline";

    editorForm.style.display = "none";
});

saveBtn.addEventListener("click", () => {
   noteForm.submit();
})