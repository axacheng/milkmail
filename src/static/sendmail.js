$(document).ready(function()
{
  $(".sendMail").click(function()
    {
      var element = $(this);
      var Id = element.attr("id");
      var SendTo = element.attr("sendto");
      $("#flash"+Id).show();
      $("#flash"+Id).hide().fadeIn(1500).html('<img src="/static/ajax-loader.gif" align="absmiddle"><font color="white" style="background: #ff0000"> Loading ....</font>');

  $.ajax({
    type: "POST",
    url: "/send/" + Id,
    data: "",
    cache: false,
    success: function(){
      $("#flash"+Id).html("<div id='message'></div>");
      $("#message").html("<b>Mail has been sent to:  </b>" + SendTo).hide().fadeIn(3000)
      
    },
    //success: function(html){
    //  $("#loadplace"+Id).append(html);
    //  $("#flash"+Id).hide();  
    //},
  });//.ajax END
  return false; //POST without doing reflash html
    
    }
  );
});