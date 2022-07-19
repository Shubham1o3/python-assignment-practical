main_status = True
while main_status:
    main_choice = int(input(""" Enter a choice :
                                1. Councellor
                                2. Student 
                                3. Exit   """))
    if main_choice==1:
        student={}

        lst=("""       Commands
                    press 1 for add student 
                    press 2 for view All student data
                    press 3 for exit          """)

        status = True
        status1=True
        sr_no = 0
        while status :
            print(lst)
            student_info={}
            choice = int(input(" Enter a choice : "))
            if choice==1:
                firstname = input(" Name of student : ")
                lastname = input(" lastname of student :")
                contact = int(input("enter a Contact Number : "))
                faculty = input(" Faculty Name that assigned : ")
                # while status1:
                #     choice_subject = {"Maths": 500,"Science":600,"Gujarati":500, "Hindi":500}
                #     selected_sub={}
                #     subject={}
                #     print(choice_subject)
                #     for i in range(len(choice_subject)):
                #         sub_choice = input(" Enter a subject : ")
                #         subject=choice_subject.get(str(sub_choice))
                #         # if sub_choice=="no" or sub_choice=="n":
                #         if sub_choice not in choice_subject.keys():
                #             if sub_choice=="n":
                #                 break
                #             else:
                #                 pass
                #         else:
                #             selected_sub[sub_choice]=subject
                #             print(selected_sub)
                #             status1=False
                
                study_fees={}
                study_marks={}
                n=int(input("Howmany subjects taht student want to choose :  "))
                i=0
                while i<n:
                    subject=input("Enter a subject name : ")
                    subject_fee = int(input("Enter a fee : "))
                    subject_marks = int(input(" Enter a Marks : "))
                    print("-------Subject fee---------")
                    study_fees[subject]=subject_fee
                    print("-------Subject Marks---------")
                    study_marks[subject]=subject_marks
                    i=i+1

                print(study_fees)
                print(study_marks)
                student_info['sr_no']=sr_no
                student_info['lastname']=lastname
                student_info['contact']=contact
                student_info['faculty']=faculty
                student_info['study_fees']=study_fees
                student_info['subject_marks']=study_marks
                # student_info['subject_fee']=subject_fee
                # student_info['subject_marks']=subject_marks
                student[firstname]=[student_info]
                print("_____>>>>><<<<<<<<___________")
                print(student)
                print("______>>>>>>>>><<<<<<<<<<_________")
                
                sr_no+=1
                    
            elif choice==2:
                for k in student.keys():
                    print("-------------->>>>><<<<<------------------")
                    print(f"student Name : {k}")
                    print("Details as per below           ---------------------------------")
                    print(student.get(k))
                print("----------@@@@@@@@----------------")
                stud_choice = input("Do you want to show data of a particular student press y for yes and n for no ")
                if stud_choice == 'yes' or stud_choice=='y':
                    j = input("Enter a Firstname : ")
                    print(student.get(j))
                else:
                    pass
                print("-------------@@@@@@@@----------------")
                remove_data=input(" Do you want to remove data of a particular student press y for yes and n for no ")
                if remove_data == 'yes' or remove_data=='y':
                    d = input(" Enter a Firstname : ")
                    print(student.pop(d))
                else:
                    pass
            else :
                status=False
    
    elif main_choice==2:
        s = input("Enter a Firstname : ")
        data={}
        data=student.get(s)
        print(data)
        a=data[0]
        print(a)
        print(type(a))
        ad=a['study_fees']
        print(ad)
        print(type(ad))
        print("Total fees : ",sum(ad.values()))
        
    else:
        main_status=False


