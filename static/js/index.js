let copyBtn = document.getElementById('copy')
copyBtn.addEventListener('click',function() {

    var copyText = document.getElementById("shortURL");

    navigator.clipboard.writeText(copyText.value).then(function() {
        alert("Copied the text: " + copyText.value);
      }, function() {
        alert("Failed to copy");
      });
})