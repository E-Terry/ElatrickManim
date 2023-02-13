---
title: "Index"
---

# Mr. Reed's Physics Class Documentation
Hopefully these resources will be helpful to y'all. Here are the things we have created:
- [Beautiful Notes](https://e-terry.github.io/ElatrickManim/notes/)
- [Mesmerizing Animations](https://e-terry.github.io/ElatrickManim/animations/)

Here's a cat picture and a dog picture while you ponder the existential dread of trying to cram for an exam:

<div id="pictues" style="display:flex; max-width:50vw;max-height:50vh">

<div id="cat-picture" style="flex:1;max-width:15vw;max-height:15vh"></div>

<script>
    $.ajax({
    url: "https://api.thecatapi.com/v1/images/search",
    success: function(data) {
        var imgUrl = data[0].url;
        $("#cat-picture").html("<img src='" + imgUrl + "' />");
    }
    });
</script>

<div id="dog-picture" style="flex:1;max-width:15vw;max-height:15vh"></div>

<script>
    $.ajax({
    url: "https://api.thedogapi.com/v1/images/search",
    success: function(data) {
        var imgUrl = data[0].url;
        $("#dog-picture").html("<img src='" + imgUrl + "' />");
    }
    });
</script>

</div>