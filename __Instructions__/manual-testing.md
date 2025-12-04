Identify and report issues in the application through manual testing
The application contains quality issues, which can be identified through manually testing the web application UI (the web pages). At least two such issues related to functionality or usability should be reported as proper bug reports with an informative title, steps to reproduce, expected results and actual behavior.

The reported issues should be more severe than minor inconveniences. For example, elements not being perfectly aligned or a search bar being slightly hard to find would be considered minor. Rather, try to find something that feels broken, such as an element that should be interactive being unresponsive, or a feature not working as expected.

Avoid reporting feature requests. You should find issues in existing features, not propose additional features to improve quality or user experience. As an example, reporting that users should be able to sort todo items or lists would be a feature request, not a bug report.

There will be no penalty for adding bug reports for minor issues, but to pass, you should find some of the more severe issues in the application. Also, reporting accessibility issues that can be automatically detected by Lighthouse won't be counted as identified issues for this project.

Despite their importance, you don't have to worry about adding additional media such as screenshots to the bug reports. The course platform does not currently support submitting binary files such as png or jpeg images (they will be corrupted).

To be sure others will be able to reproduce your issues, you should verify that they are reproducible in a fresh instance of an unmodified application (avoid using the development configuration for manual testing).