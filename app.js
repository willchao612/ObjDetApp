const axios = require('axios').create({ baseURL: 'http://localhost:5000' });

const imageInput = document.getElementById('imageInput');
const resultImage = document.getElementById('resultImage');
const submitBtn = document.getElementById('imageButton');
const ratingInput = document.getElementById('ratingInput');
const ratingButton = document.getElementById('ratingButton');
const msg = document.getElementById('msg');
const totalVisits = document.getElementById('totalVisits');
const avgRating = document.getElementById('avgRating');

document.addEventListener('DOMContentLoaded', () => {
  axios.get('/visits').then((res) => {
    totalVisits.textContent = res.data.visits + ' visits in total';
  });

  axios.get('/rating').then((res) => {
    avgRating.textContent = 'average rating: ' + res.data.score;
  });
});

submitBtn.addEventListener('click', (e) => {
  e.preventDefault();

  const formData = new FormData();
  if (imageInput.files.length !== 0) {
    formData.append('image', imageInput.files[0]);
    axios.post('/upload', formData).then((res) => {
      if (res.status === 200) {
        showMessage('image upload success');
        resultImage.style.display = 'inline';
        resultImage.src = res.data;
      } else {
        showMessage('something wrong');
      }
    });
  }
});

ratingButton.addEventListener('click', (e) => {
  e.preventDefault();

  const score = ratingInput.value;
  if (score !== '') {
    axios.post('/rating', { score: parseInt(score) }).then((res) => {
      if (res.status === 200) {
        showMessage('thank you for rating');
      } else {
        showMessage('something wrong');
      }
    });
  }
});

const showMessage = (message) => {
  msg.style.display = 'block';
  msg.textContent = message;
};
