
   var getCourse = document.getElementById('courses');
    var getUnit = document.getElementById('unit');
    var placeThings = document.getElementById('result');
    var total;
    var displayButton = document.getElementById('hidden');
    var i=0;
    var j = 0;
    var coursesOffered=0;
function GpCalc(){
    var realCourse = getCourse.value;
     var realUnit = parseInt(getUnit.value);
    var yourGrade = document.querySelector('input[name="grade"]:checked').value;
    if(( yourGrade == null) || (getUnit.value == null) || (getCourse.value == null)){
        alert("please Fill in the empty fields");

    }else{
       
    displayButton.style.display = "block";
    var createStuff = document.createElement('p');
    createStuff.setAttribute('class','created-stuff');
    createStuff.innerHTML = realCourse + '&nbsp' + realUnit +
    ' credit units ' + '<button type="button" onclick="Delete(this)">Remove</button>';
    placeThings.appendChild(createStuff);
    total = yourGrade * realUnit;
    i+=total;
    j+=realUnit;
    coursesOffered++;
    }
}
function Delete(forRemoval){
    forRemoval.parentNode.parentNode.removeChild(forRemoval.parentNode);8
}
function Calculate(){
    var cgp = i/j;
    var finalResult = cgp.toFixed(2);
     message = "You offered " + coursesOffered + " courses. Your GPA is " + finalResult;
    /*switch(cgp){
        case 1 :
         message = "you offered " + coursesOffered + " courses. your gpa is " + cgp + ".0";
        break;
        case 2 :
        message = "you offered " + coursesOffered + " courses. your gpa is " + cgp + ".0";
        break;
        case 3 :
        message = "you offered " + coursesOffered + " courses. your gpa is " + cgp + ".0";
        break;
        case 4:
        message = "you offered " + coursesOffered + " courses. your gpa is " + cgp + ".0";
        break;
        case 5:
        message = "you offered " + coursesOffered + " courses. your gpa is " + cgp + ".0";
        break
        default:
        message = "you offered " + coursesOffered + " courses. your gpa is " + cgp;
        break;
    }*/
    var displayStuff = document.getElementById('result');
    var buttonSee = document.getElementById('refresh');
    buttonSee.style.display = "block";
    displayButton.style.display = "none";
    displayStuff.innerHTML = message;
    displayStuff.style.color ="white";
    displayStuff.style.fontSize = "25px";
    displayStuff.style.textAlign = "center";
    displayStuff.style.paddingTop = "100px";
    var hide = document.getElementById('to-hide');
    hide.style.display = "none";
}