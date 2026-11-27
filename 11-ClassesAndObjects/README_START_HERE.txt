UEK - Classes and Objects / 11-ClassesAndObjects

SOURCE: Uploaded UEK exercise document 'CLASSES AND OBJECTS'.
Folder 11 is user-requested. Names follow section and task numbers:
Section 1: 1-4 through 1-9 (6 exercises)
Section 2: 2-2 (1 exercise)
Section 3: 3-1 through 3-6 (6 exercises)
Section 4: 4-4 through 4-11 (8 exercises)
21 main coding exercises. Other section items are theory, videos, examples.

RUN (from the project root):
  cd 11-ClassesAndObjects
  py 1-4.py
  py 3-6.py
  py 4-4.py

Some programs use additional modules in the SAME directory:
  3-x.py -> tv.py / tv_show.py
  4-4.py -> ebook.py
  4-5.py -> thermometer.py
  4-8.py -> smartphone.py, contact.py, contact_list.py

ORIGINALS MISSING: student.py, taxi.py, socialmedia.py and book.py
from the professor were not supplied. Exercises 1-4, 1-6, 1-7, 1-8
are clean independent implementations reflecting described requirements,
not exact modifications of original files.

Notes:
- 3-1 through 3-6 share one final version of the TV class in tv.py.
  This meets final functional requirements; it does not preserve six
  separate historical intermediate TV class definitions.
- 4-5 thermometer measurements are randomly simulated, not medical data.
- 4-6 stores currency using Decimal to avoid float precision issues.
- 4-7 accepts optional user input; press Enter for assigned sample values.
- 4-9 is named C as explicitly required.

Use 'python -m compileall -q .' to check syntax, and run each task
for actual behavior. Check assignment-specific requirements before submitting.
