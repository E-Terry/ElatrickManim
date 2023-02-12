---
title: "Index of Resources"
---

# Mr. Reed's Physics Class Documentation
Hopefully these resources will be helpful to y'all. Here are the things we have created:
- [Beautiful Notes](https://e-terry.github.io/ElatrickManim/notes/)
- [Mesmerizing Animations](https://e-terry.github.io/ElatrickManim/animations/)

Here's a cat picture while you ponder the existential dread of trying to cram for an exam:

<div id="cat-picture"></div>

<script>
    $.ajax({
    url: "https://api.thecatapi.com/v1/images/search",
    success: function(data) {
        var imgUrl = data[0].url;
        $("#cat-picture").html("<img src='" + imgUrl + "' />");
    }
    });
</script>