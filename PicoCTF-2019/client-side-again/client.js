var string_list = [
  "29871}",
  "_again_d",
  "this",
  "Password\x20Verified",
  "Incorrect\x20password",
  "getElementById",
  "value",
  "substring",
  "picoCTF{",
  "not_this"
];
(function(arg1, arg2) {
  var f1 = function(arg3) {
    while (--arg3) {
      arg1.push(arg1.shift());
    }
  };
  f1(++arg2);
})(string_list, 0x1b3);
var function1 = function(arg1, not_used) {
  return string_list[arg1];
};
function verify() {
  checkpass = document[function1("0")]("pass")[function1("1")];
  split = 0x4;
  if (checkpass[function1("0x2")](0, split * 0x2) == function1("0x3")) {
    if (checkpass[function1("0x2")](0x7, 0x9) == "{n") {
      if (
        checkpass[function1("0x2")](split * 0x2, split * 0x2 * 0x2) ==
        function1("0x4")
      ) {
        if (checkpass[function1("0x2")](0x3, 0x6) == "oCT") {
          if (
            checkpass[function1("0x2")](split * 0x3 * 0x2, split * 0x4 * 0x2) ==
            function1("0x5")
          ) {
            if (checkpass["substring"](0x6, 0xb) == "F{not") {
              if (
                checkpass[function1("0x2")](
                  split * 0x2 * 0x2,
                  split * 0x3 * 0x2
                ) == function1("0x6")
              ) {
                if (
                  checkpass[function1("0x2")](0xc, 0x10) == function1("0x7")
                ) {
                  alert(function1("0x8"));
                }
              }
            }
          }
        }
      }
    }
  } else {
    alert(function1("0x9"));
  }
}
