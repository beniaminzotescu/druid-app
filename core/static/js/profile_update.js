$(document).ready(function() {
  // Initial state
  var isEditMode = false;

  // Edit button click event
  $('#edit-btn').click(function() {
    isEditMode = true;
    toggleEditMode();
  });

  // Cancel button click event
  $('#cancel-btn').click(function() {
    isEditMode = false;
    toggleEditMode();
  });

  // Toggle edit mode function
  function toggleEditMode() {
    if (isEditMode) {
      $('.profile-avatar').hide();
      $('#profile-details').hide();
      $('#edit-buttons').hide();
      $('#profile-update-form').show();
    } else {
      $('.profile-avatar').show();
      $('#profile-details').show();
      $('#edit-buttons').show();
      $('#profile-update-form').hide();
    }

    // Show/hide the "Editează" button based on the edit mode
    if (isEditMode) {
      $('#edit-btn').hide();
    } else {
      $('#edit-btn').show();
    }
  }
});
