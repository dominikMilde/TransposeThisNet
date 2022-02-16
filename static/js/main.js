$(document).ready(function(){
    $("span").dblclick(function () {
       this.classList.toggle("chord");
    });

    $('#btnCopy').click(function () {
        copyToClipboard("copyArea");
    });


    function copyToClipboard(containerid) {
        if (document.selection) {
            var range = document.body.createTextRange();
            range.moveToElementText(document.getElementById(containerid));
            range.select().createTextRange();
            document.execCommand("copy");
            alert("Lyrics copied!");

        } else if (window.getSelection) {
            var range = document.createRange();
            range.selectNode(document.getElementById(containerid));
            window.getSelection().addRange(range);
            document.execCommand("copy");
            alert("Lyrics copied");
        }}

    $('#btnHide').click(function () {
        //alert("sakrij");
        if ($('#mainNavBar').is(":visible")) {
            $('nav').hide("slow");
        } else {
            $('nav').show();
        }
    });

    $(window).resize(function() {
        if ($(this).width() < 770) {
            $('nav').hide("slow");
        } else {
            $('nav').show();
        }
    });
    if ($(this).width() < 770) {
        $('nav').hide();
    } else {
        $('nav').show();
    }

    var transposeNow = 0;
    var steps;
    $('#six').click(function() {
        steps = 6-transposeNow;
        transposeNow = 6;
        $('li.transpose').each(function () {
            this.classList.remove("active");
        });
        $(".chord").each(function(){
            transpose($(this), steps)});
        this.classList.add("active");
    });
    $('#five').click(function() {
        steps = 5-transposeNow;
        transposeNow = 5;
        $('li.transpose').each(function () {
            this.classList.remove("active");
        });
        $(".chord").each(function(){
            transpose($(this), steps)});
        this.classList.add("active");
    });
    $('#four').click(function() {
        steps = 4-transposeNow;
        transposeNow = 4;
        $('li.transpose').each(function () {
            this.classList.remove("active");
        });
        $(".chord").each(function(){
            transpose($(this), steps)});
        this.classList.add("active");
    });
    $('#three').click(function() {
        steps = 3-transposeNow;
        transposeNow = 3;
        $('li.transpose').each(function () {
            this.classList.remove("active");
        });
        $(".chord").each(function(){
            transpose($(this), steps)});
        this.classList.add("active");
    });
    $('#two').click(function() {
        steps = 2-transposeNow;
        transposeNow = 2;
        $('li.transpose').each(function () {
            this.classList.remove("active");
        });
        $(".chord").each(function(){
            transpose($(this), steps)});
        this.classList.add("active");
    });
    $('#one').click(function() {
        steps = 1-transposeNow;
        transposeNow = 1;
        $('li.transpose').each(function () {
            this.classList.remove("active");
        });
        $(".chord").each(function(){
            transpose($(this), steps)});
        this.classList.add("active");
    });
    $('#zero').click(function() {
        steps = 0-transposeNow;
        transposeNow = 0;
        $('li.transpose').each(function () {
            this.classList.remove("active");
        });
        $(".chord").each(function(){
            transpose($(this), steps)});
        this.classList.add("active");
    });
    $('#_one').click(function() {
        steps = -1-transposeNow;
        transposeNow = -1;
        $('li.transpose').each(function () {
            this.classList.remove("active");
        });
        $(".chord").each(function(){
            transpose($(this), steps)});
        this.classList.add("active");
    });
    $('#_two').click(function() {
        steps = -2-transposeNow;
        transposeNow = -2;
        $('li.transpose').each(function () {
            this.classList.remove("active");
        });
        $(".chord").each(function(){
            transpose($(this), steps)});
        this.classList.add("active");
    });
    $('#_three').click(function() {
        steps = -3-transposeNow;
        transposeNow = -3;
        $('li.transpose').each(function () {
            this.classList.remove("active");
        });
        $(".chord").each(function(){
            transpose($(this), steps)});
        this.classList.add("active");
    });
    $('#_four').click(function() {
        steps = -4-transposeNow;
        transposeNow = -4;
        $('li.transpose').each(function () {
            this.classList.remove("active");
        });
        $(".chord").each(function(){
            transpose($(this), steps)});
        this.classList.add("active");
    });
    $('#_five').click(function() {
        steps = -5-transposeNow;
        transposeNow = -5;
        $('li.transpose').each(function () {
            this.classList.remove("active");
        });
        $(".chord").each(function(){
            transpose($(this), steps)});
        this.classList.add("active");
    });
});

function transpose(chord, steps) {
    var chordList = ["C", "C", "C#", "Db", "D", "D", "D#", "Eb", "E", "E", "F", "F", "F#", "Gb", "G", "G", "G#", "Ab", "A",
        "A", "A#", "Bb", "B", "B", "C", "C", "C#", "Db", "D", "D", "D#", "Eb", "E", "E", "F", "F", "F#", "Gb",
        "G", "G", "G#", "Ab", "A", "A", "A#", "Bb", "B", "B", 'c', 'c', 'c#', 'db', 'd', 'd', 'd#', 'eb', 'e', 'e', 'f',
        'f', 'f#', 'gb', 'g', 'g', 'g#', 'ab', 'a', 'a', 'a#', 'bb', 'b', 'b', 'c', 'c', 'c#', 'db', 'd', 'd', 'd#', 'eb',
        'e', 'e', 'f', 'f', 'f#', 'gb', 'g', 'g', 'g#', 'ab', 'a', 'a', 'a#', 'bb', 'b', 'b'];

    var step;
    if (steps<0) {
        step = steps + 12;
    }
    else{
       step = steps;
    }

    var tekst = chord.text();
    var indSlashOld = 0;
    //SEARCHING FOR "MIXED" CHORDS

    //first case, one letter chords
    if (tekst.length === 1) {
        //alert(tekst + " first");
        var chordIndex = chordList.indexOf(tekst);
        chord.text(chordList[chordIndex + step * 2]);
    }

    else {
        if (tekst[1] === "#" || tekst[1] === "b") {
            //alert(tekst + " second");
            var changeOld = tekst[0].concat(tekst[1]);

            chordIndex = chordList.indexOf(changeOld);
            var changeNew = tekst.replace(changeOld, chordList[chordIndex + step * 2]);
            chord.text(changeNew);
        }
        else {
            //alert(tekst + " third");
            var changeOld = tekst[0];
            chordIndex = chordList.indexOf(changeOld);
            var changeNew = tekst.replace(changeOld, chordList[chordIndex + step * 2]);
            chord.text(changeNew);
        }
    }
    var tekstChanged = chord.text();
    for (var i = 0; i < tekstChanged.length; i++) {
        if (tekstChanged[i] === '/') {
            indSlashOld = i;
            break;
        }
    }

    if (indSlashOld > 0) {
        var changeOld = tekstChanged.substring(indSlashOld+1, tekstChanged.length);
        //alert("found " + changeOld);
        var noChange = tekstChanged.substring(0, indSlashOld+1);
        //alert(noChange);
        var chordIndex = chordList.indexOf(changeOld);
        var changeNew = noChange.concat(chordList[chordIndex + step*2]);
        chord.text(changeNew);
    }
}