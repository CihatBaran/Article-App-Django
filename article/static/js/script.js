const selector = {
  deleteButton: document.getElementById('delete_me'),
  cancel_me: document.getElementById('cancel-me'),
  backdropSheet: document.querySelector('.backdrop--sheet'),
  confirmingPage: document.querySelector('.confirming--page'),
};
selector.deleteButton.addEventListener('click', (e) => {
  e.preventDefault();
  selector.backdropSheet.style.display = 'block';
  selector.confirmingPage.style.display = 'block';
});

selector.confirmingPage.addEventListener('click', () => {
  selector.backdropSheet.style.display = 'none';
  selector.confirmingPage.style.display = 'none';
});

selector.cancel_me.addEventListener('click', () => {
  selector.backdropSheet.style.display = 'none';
  selector.confirmingPage.style.display = 'none';
});
