const container1 = document.querySelector('.container1');
const panels = document.querySelectorAll('.panel');

container.addEventListener('click', function (e) {
  let clickedPanel = null;
  if (e.target.tagName == 'H2') {
    clickedPanel = e.target.parentNode;
  } else {
    clickedPanel = e.target;
  }
  removeActive();
  clickedPanel.classList.add('active');
});

function removeActive() {
  panels.forEach((panel) => {
    panel.classList.remove('active');
  });
}