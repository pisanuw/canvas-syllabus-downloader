### **Course Information**

This is an introductory course into the fundamentals of digital hardware, the architecture of modern microprocessors and assembly language programming. This course will provide students with the basic theories and concepts of how hardware and software cooperatively interact to accomplish real-world tasks. Elements of the hardware development such as instruction set architecture, memory and I/O organization will be examined in the context of modern computer system fundamentals such as memory management, Algorithmic state machines and Interrupt handling. Also, the differences between the CISC and RISC architectures will be examined in the context of their assembly language instruction sets and the compiler technology required to support them.  


We will first explore the elements of the modern computing system and computer arithmetic, which will be the basis of how to control the hardware elements at the assembly language level. Next, we will write some assembly language programs and then map these programs onto their analogs in higher level languages, such as C or C++. Working with assembly language will provide the insight into how modern operating systems deal with the real world through its drivers and interrupt handler routines. After understanding the assembly language, we will examine each hardware elements both at the levels of the logic gate and the basic blocks of hardware. This will lead us to look at the algorithmic state machine and how it enables a computer actually work.  Finally, we will study how to compose a micro professing unit (MPU) of these elements and connect the MPU to memory and I/O peripherals, which complete an entire computer system.

###  

### L**earning objectives for this course:**

  * Demonstrate the ways that the atomic elements of computer hardware, logic gates, are used, and detail the rules that govern their operation,

  * Understand the electronic circuit basis for modern computer systems,

  * Learn the principles of Boolean Algebra to manipulate and simplify logical equations and convert them to electronic gate circuits,

  * Develop familiarity with the concepts of synchronous logic and how it forms the basis for the operation of computer systems,

  * Be able to create simple state machines and abstract their operation to the operation of a computer system,

  * Understand the logical operation of memory systems and be able to design simple memories,

  * Describe the relationship between a computer's instruction set architecture and its assembly language instruction set,

  * Be able to write significant programs in assembly language,

  * Understand how real-world devices are interfaced to a computer system (as I/O peripherals),

  * (Learn the principles of pipelines and virtual memory if time allows.)  



  


### **Class Information**

CSS 422 TTh 11:00 am – 1:00 pm at UW2-131   


Class website: https://canvas.uw.edu/courses/1608378

Office Hours: TTh 10:30-11:00am (UW1-271T) and 1:00-1:15pm (outside of the classroom or UW1-271T) or by appointment (through Zoom)  


### **Instructor**

**Munehiro Fukuda  
**

Email: [mfukuda@uw.edu](mailto:mfukuda@uw.edu) ([CSS422] Must show on subject)

Office: **UW1-271T or by appointment (through Zoom)  
**

**Send Email (done not use the canvas inbox) !**

Emails will be the best way to reach out to me. Please include [CSS422] at the beginning of the subject to avoid going to the junk folder.  

### **Prerequisites**

  * CSS 342




**Textbooks**

We mainly use the first two textbooks. 

  * Essentials of Computer Organization & Architecture (5th edition), Linda **Null** and Julia **Lobur** , ISBN: 9781284123036
  * ARM Microprocessor Systems, Muhammad **Tahir** and Kashif **Javed** , ISBN: 9781482259384 (paper), 9781482259391 (electronic)




 

## **  Grading Policy**

**Course Work** |  **%**  
---|---  
Exams |  50  
Project |  16.5  
Homework |  24  
Participation (In-Class Discussions and Labs, each with 0.5%  
|  9.5  
**Total** |  100  
  
 

**Achievements** |  **Estimated Grade**  
---|---  
90s |  3.5 - 4.0  
80s |  2.5 - 3.4  
  
70s  
|  1.5 - 2.4  
60s (62 or above)  
|  0.7- 1.4  
Below 62  
|  0.0  
  
  
 

If you disagree with your grade for each assignment, please bring the issue to my attention **within a week after I returned the graded work to you.** Once this grace period has passed, no more regrading discussions. I will review your grade and I will either correct it, reject it, or pass it back to the grader to reconsider. In any case, I am the one who makes the final decision. 

  


### **Class Policies**

  * **Exams** : You are given midterm and final exams. Midterm exam covers the contents you have learned in class by the time of the exam. Final exam will cover the contents after the midterm, while some questions may be based on your knowledge in the first 5 weeks. The exams are not testing your memory; they test your understanding of the concepts. You should expect challenging questions that apply basic concepts to comprehensive problems. No cheating whatsoever!! If I see any suspicious actions during exam, then you will be asked to leave the exam room, and you will be reported as cheating. (See "Academic Integrity" for details)


  * **Project** : A significant effort will be involved in the class project. The final project is done independently, in other words **in solo work**.  





The project is the capstone element of the course. It is designed to bring together the following elements:

  * Developing an architectural understanding of a popular computer architecture  

  * Understanding assembly language supports for operating systems and compilers
  * Solidifying your command of assembly language coding methods



The project is due at the 11th week. The project is graded based on a midpoint report and the final product.  


  * **Participation:  **Class participation is important. The professor will check your active participation through your activities on Google Doc and lab submission as well as in-class discussions (weeks 1 - 10).   

    * **Lab** :  You are required to participate in in-class lab work and submit your work to Canvas.   

    * **Exercise** : Short answer questions will be given in class as exercises. You'll make a group of 4-5 students to solve questions in collaboration. Each group will submit the answer through Google Doc.  



  * **Homework** : Homework assignments are an _**integral part**_  of the course and are designed to emphasize the material covered in classroom discussions. Note that homework assignments are not simple problems asking definition of terms. Most homework questions will be challenging as you have to APPLY what you have learned in class in real problems. You are supposed to solve the questions, not searching the questions!!  Any late homework will**  not be accepted in any circumstances, which means you will be given zero for the late homework. **



 

### **Lectures**

All the lecture slides will be made available to the students at the "File" at least a week before the corresponding class date. My expectation is that you should check the slides and read the corresponding textbook/reference/manual chapters before coming to class. You don't have to understand everything before the class. That's why lectures intend to assist you in full understanding.   


 

### **Articles**

Other instructors previously required to read the articles, but I will not make this a requirement in this class. However, all the articles will be directly related to the contents in this course, so I recommend you read them.

 

### [**Software**](https://canvas.uw.edu/courses/1444198/pages/software "Software")

We will use the following three software tools:

  1. VisUAL (<https://salmanarif.bitbucket.io/visual/>): a very handy ARM simulator that supports a subset of ARM CPU instructions.  

  2. Keil uVersion (<https://www2.keil.com/mdk5/uvision/>): a free version of Keil MDK that simulates a real ARM processor.
  3. Logisim (<http://www.cburch.com/logisim/>): an educational tool for designing and simulating digital logic circuits.  




All software are installed on UW1-310 Windows Machines. Since all these simulators are free, if you have a Windows machine or a VM on Mac, you can install them by yourself. Please note that Logisim is available on both Windows and MacOS. We will use VisUAL in lab 1a and HW2-3; Keil uVersion in lab 1b, HW4, and the final project; and LogiSim in lab 2a-2b and HW5-7.

###  

### **Academic Integrity**

All students are expected to abide by the published rules of student conduct. Your work, unless you are involved in a designated group project, is expected to be your own work. Plagiarism and cheating undermine the values of the university. They are a serious breach of trust and will not be tolerated. If you are ever in doubt, consult  the University Policies <http://www.washington.edu/admin/rules/policies/WAC/478-121TOC.html> in your Student Handbook. 

Forming a discussion group can be a very beneficial activity and a good way to learn. Discussing the material with your classmates, if done properly and conscientiously, can be a very effective learning tool. Also, helping each other to learn can be a particularly satisfying task. However,**  copying each other's homework assignments is not a good way to make use of your discussion group and all students found to have shared homework assignments will be dealt with.** In general, your homework assignments are your personal intellectual property. Do not share the content of your assignments with any other student.

The literature is full of a great variety of very good and efficient algorithms. Taking advantage of these is common practice. However, for any such code you use, you must cite the source**…you will be given a failing mark on the homework or project if you do not cite your sources in your listing - this is not something to be hand written in after the fact, it must be included in your source code…** This is an easy step that you should get in the habit of doing… Please note very carefully, this **_does not_**  include your fellow class mate's code.

In summary, take some free advice from me. Don't cheat. I will catch students cheating and will follow the university guidelines to the letter. 

 

### **Attendance**

Just simple attendances are not really useful. Of importance however is your contribution to making the class academically stimulating and intellectually live. This include your in-class exercises and labs, both considered as part of your grade. Please be reminded that in-class exercises and labs are not always conducted as scheduled. If you miss a class, you might miss exercises and/or labs. Only if you had to miss the class because of sickness, family emergency, or inevitable business/work-specific events, (e.g., meetings or trips), you may bring your late exercise or lab work to me within a week, together with a letter of proof written by your MD, family member, or company. Needless to say, if you miss a class session you are still responsible for all the material covered in that lecture.  


Class participation can enhance your grade. If you're going to come to class and then tune-out, quite frankly, you're wasting your time. Your time is your most valuable asset, don't waste it. Although attendance does not count towards your final grade, class participation can count in a positive way. If you're not here, you can't participate. ****

Finally, expectations for behavior in class are no different than expectations for behavior in the real world. Meeting rooms at many high-tech companies often have a posted list of meeting expectations and behaviors. My expectations are as follows:

  * Come to class on time and ready to participate. If you are late, I reserve the right to ask you to leave and return in an hour when the class takes a mid-lecture break.
  * Come prepared for the day's lecture
  * **No web surfing, instant messages, or e-mail during class**
  * **In particular, turn off (or sound off) all cell phones and pagers**
  * Return promptly from mid-class breaks
  * Raise your hand to be recognized



A special word about cell phones: A cell phone that rings during class is indicative of the highest level of bad manners. When your cell phone rings you are disrupting the class. I will take particular note of the owner of a ringing cell phone.

_**Laptops, whether plugged into the network, or wireless, should only be used for activities directly related to this class. If you must surf the internet, or i**_ _**f you have to do instant messaging or send e-mail then please leave the room.**_

_**Unlike the other professors, whenever I find students whose in-class behaviors are not appropriate, I kick them out of the classroom immediately.**_

 

### **Disability Resources/Religious Accommodation  
**

**Access and Accommodations** : Your experience in this class is important to me. If you have already established accommodations with Disability Resources for Students (DRS), please communicate your approved accommodations to me at your earliest convenience so we can discuss your needs in this course.

If you have not yet established services through DRS, but have a temporary health condition or permanent disability that requires accommodations (conditions include but not limited to; mental health, attention-related, learning, vision, hearing, physical or health impacts), you are welcome to contact DRS at 425-352-5307 or [uwbdrs@uw.edu](mailto:uwbdrs@uw.edu). DRS offers resources and coordinates reasonable accommodations for students with disabilities and/or temporary health conditions. Reasonable accommodations are established through an interactive process between you, your instructor(s), and DRS. It is the policy and practice of the University of Washington to create inclusive and accessible learning environments consistent with federal and state law.

 

**The class follows the religious accommodation policy. Please check<https://registrar.washington.edu/staffandfaculty/religious-accommodations-policy/>**

 

## **Parenting Students**

Parenting students are encouraged to take advantage of the resources provided on campus. These resources include the Parent Union at UWB, the Childcare Assistance Program, on-campus Family Friendly Spaces, priority access at Bright Horizons Bothell and Bothell KinderCare, and back-up/sick care at one of these locations. On campus resources include lactation rooms and baby changing stations. For more detailed information, contact the Parent Union on Facebook: <https://www.facebook.com/PUUWB>[ (Links to an external site.)Links to an external site.](https://www.facebook.com/PUUWB).

 

### **Remark**

  * This syllabus represents a general plan for the course and deviations from this plan may be necessary during the duration of the course.
  * Your constructive assessment of this course plays an indispensable role in shaping education at Washington State. When you are asked to do, please take time to fill out the course evaluation.


