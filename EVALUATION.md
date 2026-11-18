1) The prompt I used was "Here is my project, these are the next steps, provide code for the 2 new files." and I uploaded the word doc provided.
2) the code I ended up with was a test for looking up an offical name, alias, case insensativity, a not found resource, and testing all 5. It would then return the results of the tests.
3) I verified the results by double checking the JSON file. I checked for the health center, academic advisment, and the dental office. I also changed a few of the resources to force some errors to check if it was working correctly. After that I used different resources to verify again.
4) I did not change anything, the generated code seemed to add no slop.
5) The YAML was generated from the original prompt.
6) Everytime I push to main, has an action start a clean ubunu machine, it checks out the repository, installs python and pytest. It then runs the tests, and if any test fails it marks it as such in the actions tab.
7) I also did not change anything here, as the code was streamlined and worked without error.