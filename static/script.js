

const uploadBtn = document.getElementById("uploadBtn");
const fileInput = document.getElementById("fileInput");
const status = document.getElementById("status");
const loadBtn = document.getElementById("loadBtn");
const candidateList = document.getElementById("candidateList");



uploadBtn.addEventListener("click", async () => {
  if (!fileInput.files.length) {

  status.textContent = "Please choose a file first";
  return
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  status.textContent = "Uploading...";

  const response = await fetch("/upload", {
    method: "POST",
    body: formData
  });

  const data = await response.json();
  console.log(data);

  status.textContent = "Upload successful!";

});


loadBtn.addEventListener("click", async () => {
  candidateList.textContent = "Loading...";

  const response = await fetch("/candidates");
  const data = await response.json();

  console.log(data);

  candidateList.textContent = JSON.stringify(data, null, 2);
});