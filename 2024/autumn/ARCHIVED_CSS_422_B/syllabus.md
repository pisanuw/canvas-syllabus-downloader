## Overview 

  * **Instructor:**  Yusuf Pisan [pisan@uw.edu](mailto:pisan@uw.edu)
    * [Homepage](https://pisanorg.github.io/yusuf/) || [Research Group](https://t4guw.github.io/) || [All Course Evaluations](https://pisanorg.github.io/yusuf/teaching/evaluations/) || [RateMyProfessors](https://www.ratemyprofessors.com/professor/2274276)
  * **Office hours:** Monday 4:00-5:00pm, Thursday 2:00-3:00pm at UW1-260Q. Signup via [Canvas Calendar](https://canvas.uw.edu/calendar)
  * **Class Sessions:** Tuesday/Thursday 11:00am-1:00pm in UW1-110
  * **Prerequisite:**  CSS 342.
  * [Course website](https://canvas.uw.edu/)
  * **Class Discord** : <https://discord.gg/5mEm92e> 
  * You can submit [anonymous feedback](https://bit.ly/ypmuddy) for this class anytime during the quarter



### **Course Information**

This is an introductory course into the fundamentals of digital hardware, the architecture of modern microprocessors and assembly language programming. This course will provide students with the basic theories and concepts of how hardware and software cooperatively interact to accomplish real-world tasks. Elements of the hardware development such as instruction set architecture, memory and I/O organization will be examined in the context of modern computer system fundamentals such as memory management, Algorithmic state machines and Interrupt handling. Also, the differences between the CISC and RISC architectures will be examined in the context of their assembly language instruction sets and the compiler technology required to support them.  


We will first explore the elements of the modern computing system and computer arithmetic, which will be the basis of how to control the hardware elements at the assembly language level. Next, we will write some assembly language programs and then map these programs onto their analogs in higher level languages, such as C or C++. Working with assembly language will provide the insight into how modern operating systems deal with the real world through its drivers and interrupt handler routines. After understanding the assembly language, we will examine each hardware elements both at the levels of the logic gate and the basic blocks of hardware. This will lead us to look at the algorithmic state machine and how it enables a computer actually work.  Finally, we will study how to compose a micro professing unit (MPU) of these elements and connect the MPU to memory and I/O peripherals, which complete an entire computer system.

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





**Textbooks**

We mainly use the first two textbooks. 

  * Essentials of Computer Organization & Architecture (5th edition), Linda **Null** and Julia **Lobur** , ISBN: 9781284123036
  * ARM Microprocessor Systems, Muhammad **Tahir** and Kashif **Javed** , ISBN: 9781482259384 (paper), 9781482259391 (electronic)




## **  Grading Policy**

**Course Work** |  **%**  
---|---  
Exams |  50  
Project |  20  
Homework |  20  
Participation (In-Class Discussions and Labs)  
|  10  
**Total** |  100  
  
 

A scale of 90s (3.5‐4.0), 80s (2.5‐3.4), 70s (1.5‐2.4), 60s (0.5‐1.4) is a rough guide. A student who achieves 75% will receive a minimum of 2.0, 85% will receive a minimum of 3.0 and 95% and above will receive a 4.0 grade. Scores in between will be interpolated.

If you disagree with your grade for each assignment, please bring the issue to my attention **within a week after I returned the graded work to you.** Once this grace period has passed, no more regrading discussions. I will review your grade and I will either correct it, reject it, or pass it back to the grader to reconsider. In any case, I am the one who makes the final decision. 

  


### **Class Policies**

  * **Exams** : You are given two exams. Exam covers the contents you have learned in class by the time of the exam. Second exam will cover the contents after the first exam, while some questions may be based on your knowledge in the first 5 weeks. The exams are not testing your memory; they test your understanding of the concepts. You should expect challenging questions that apply basic concepts to comprehensive problems. 
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



### **Software**

We will use the following three software tools:

  1. VisUAL (<https://salmanarif.bitbucket.io/visual/>): a very handy ARM simulator that supports a subset of ARM CPU instructions.  

  2. Keil uVersion (<https://www2.keil.com/mdk5/uvision/>): a free version of Keil MDK that simulates a real ARM processor.
  3. Logisim (<http://www.cburch.com/logisim/>): an educational tool for designing and simulating digital logic circuits.  




All software are installed on UW1-310 Windows Machines. Since all these simulators are free, if you have a Windows machine or a VM on Mac, you can install them by yourself. Please note that Logisim is available on both Windows and MacOS. We will use VisUAL in lab 1a and HW2-3; Keil uVersion in lab 1b, HW4, and the final project; and LogiSim in lab 2a-2b and HW5-7. 

## Getting Help 

There are multiple ways of getting help:

  * **Discord**



With an active class, discord can be one of the easiest and fastest ways to get help. Discord channel is an extension of our class and the same rules for in-class behavior apply to discord. I will also monitor the discord channel and contribute to the discussion from time to time. When asking questions:

  *     * **Do not**  post code.
    * Be clear in stating the problem. Explain how you tried to solve it. Make sure the answer is not the first link that comes up in a Google search.
    * You can post a warning/error message from compiler and ask how others have resolved it.
    * You can ask how a specific C++ function gets used
    * You can discuss your approach in high-level terms
    * If you post a question and then figure out the answer, post your answer so it benefits others in the class



In general, if you can discuss the problem in English without having to show code, you can discuss it on Discord.

  * **QSC**



[Quantitative Skills Center](https://www.uwb.edu/academic-support-programs/qsc) has dedicated hours with 342 tutors that can help. Here is a [video about QSC services](https://urldefense.com/v3/__https://youtu.be/kKwIxylCv5c__;!!K-Hz7m0Vt54!mn6EYyQ0Jrop0WjZAP9uyfK6RFNMXB29Qqgwn4T4_AXOWIJfYBZ24l_zdbmYTAVsgIP6y48vsJjJBw%24) and the [tutoring hours](https://www.uwb.edu/academic-support-programs/qsc/schedule/css).

  * **Office Hours**



If you need extra time after office hours and cannot get your issues resolved over discord, you can setup a meeting over zoom by sending me email (pisan@uw.edu). I will not debug your code, but I will answer questions and try to help you figure out the problem. I will always ask what you have already done so far to solve the problem, so come prepared.

If you have a personal matter, please see me in office hours.

  * **Email**



Email is not an effective way to get help. Unless your question is of personal nature, it should be posted on discord. If you believe the question really needs my attention, you can tag me on discord.

### **Academic Integrity**

All students are expected to abide by the published rules of student conduct. Your work, unless you are involved in a designated group project, is expected to be your own work. Plagiarism and cheating undermine the values of the university. They are a serious breach of trust and will not be tolerated. If you are ever in doubt, consult  the University Policies <http://www.washington.edu/admin/rules/policies/WAC/478-121TOC.html> in your Student Handbook. 

Forming a discussion group can be a very beneficial activity and a good way to learn. Discussing the material with your classmates, if done properly and conscientiously, can be a very effective learning tool. Also, helping each other to learn can be a particularly satisfying task. However,**  copying each other's homework assignments is not a good way to make use of your discussion group and all students found to have shared homework assignments will be dealt with.** In general, your homework assignments are your personal intellectual property. Do not share the content of your assignments with any other student.

The literature is full of a great variety of very good and efficient algorithms. Taking advantage of these is common practice. However, for any such code you use, you must cite the source**.** This is an easy step that you should get in the habit of doing.

### **Attendance**

Just simple attendances are not really useful. Of importance however is your contribution to making the class academically stimulating and intellectually live. This include your in-class exercises and labs, both considered as part of your grade. Please be reminded that in-class exercises and labs are not always conducted as scheduled. If you miss a class, you might miss exercises and/or labs. Only if you had to miss the class because of sickness, family emergency, or inevitable business/work-specific events, (e.g., meetings or trips), you may bring your late exercise or lab work to me within a week. Needless to say, if you miss a class session you are still responsible for all the material covered in that lecture.  


Class participation can enhance your grade. If you're going to come to class and then tune-out, quite frankly, you're wasting your time. Your time is your most valuable asset, don't waste it. Although attendance does not count towards your final grade, class participation can count in a positive way. If you're not here, you can't participate. ****

Finally, expectations for behavior in class are no different than expectations for behavior in the real world. Meeting rooms at many high-tech companies often have a posted list of meeting expectations and behaviors. My expectations are as follows:

  * Come to class on time and ready to participate. If you are late, I reserve the right to ask you to leave and return in an hour when the class takes a mid-lecture break.
  * Come prepared for the day's lecture
  * No web surfing, instant messages, or e-mail during class
  * Return promptly from mid-class breaks
  * Raise your hand to be recognized



### **Disability Resources/Religious Accommodation  
**

**Access and Accommodations** : Your experience in this class is important to me. If you have already established accommodations with Disability Resources for Students (DRS), please communicate your approved accommodations to me at your earliest convenience so we can discuss your needs in this course.

If you have not yet established services through DRS, but have a temporary health condition or permanent disability that requires accommodations (conditions include but not limited to; mental health, attention-related, learning, vision, hearing, physical or health impacts), you are welcome to contact DRS at 425-352-5307 or [uwbdrs@uw.edu](mailto:uwbdrs@uw.edu). DRS offers resources and coordinates reasonable accommodations for students with disabilities and/or temporary health conditions. Reasonable accommodations are established through an interactive process between you, your instructor(s), and DRS. It is the policy and practice of the University of Washington to create inclusive and accessible learning environments consistent with federal and state law.

 

**The class follows the religious accommodation policy. Please check<https://registrar.washington.edu/staffandfaculty/religious-accommodations-policy/>**

 

## **Parenting Students**

Parenting students are encouraged to take advantage of the resources provided on campus. These resources include the Parent Union at UWB, the Childcare Assistance Program, on-campus Family Friendly Spaces, priority access at Bright Horizons Bothell and Bothell KinderCare, and back-up/sick care at one of these locations. On campus resources include lactation rooms and baby changing stations. For more detailed information, contact the Parent Union on Facebook: <https://www.facebook.com/PUUWB>

### **UWB CARE Team**

UWB CARE Team is the contact point for providing support for students. <https://www.uwb.edu/student-affairs/care-team> CARE Team is also able to provide "Emergency Funding" up to $1000 to students that can be used to help pay for textbooks, utility bills, medical bills, etc. To access the emergency funds, students need to go to <https://www.uwb.edu/student-affairs/care-team> and click on "online report" and enter their details. The same form can also be used by faculty and staff to report any concerns.

### **Remarks**

See the [School of STEM Course Policies](https://www.uwb.edu/stem/undergraduate/resources/policies-and-procedures), which covers:

  * Academic Integrity
  * Access and Accommodations
  * Classroom Emergency Preparedness
  * For Our Veterans
  * Grade of Incomplete
  * Inclement Weather
  * Parenting Resources
  * Religious Accommodations
  * Respect for Diversity
  * Student Support Services
  * Surviving Sexual and Relationship Violence
  * Wonder How to Address Faculty?



 

  * This syllabus represents a general plan for the course and deviations from this plan may be necessary during the duration of the course.
  * Your constructive assessment of this course plays an indispensable role in shaping education at Washington State. When you are asked to do, please take time to fill out the course evaluation.


