$(document).ready(function(){
 // once the document is loaded
   $('form').submit(function(){
      // there are three arguments that we are passing into $.post function
      //     1. the url we want to go to: '/posts/create'
      //     2. what we want to send to this url: $(this).serialize()
      //            $(this) is the form and by calling .serialize() function on the form it will
      //            send post data to the url with the names in the inputs as keys
      //     3. the function we want to run when we get a response:
      //            function(res) { $('#notes').html(res) }
      $.post('/posts/create', $(this).serialize(), function(res) {
        console.log($(this).serialize());
        $('#notes').html(res);
      });
      // we have to return false for it to be a single page application because without it jQuery's
      // submit function will cause a refresh of the page which would defeat the point of AJAX
      return false;
	});
});
