similar_list_ratio=[]
result_points=[]
##these are different answers given by a student
student_as=[['a b c d'],['w y x'],['t t y u'],['x v r t']]
##correct answers given by a tutor or lecturer or teacher
lec_as=[['a b d e'],['a b c x'],['x y z'],['r v l'],['p q r'],['v h k'],['t n m o'],['o q s t']]
##function to pass both student answers and lecturer answers
def compare(s_answer, l_answer):
      ##for every student answer that is not right, it must be check against lectures.
      ##len(s_answer ) mean student answers 4 in our case
      for i in range (len(s_answer)):
            ##len(l_answer ) mean lect answers 8 in our case
            for j in range(len(l_answer)):
                  ##function are tokenized each sentences to individual words
                  def convert(lst):
                     return ([i for item in lst for i in item.split()])
                  ##specific sentence for lect or student are store in right answers and stude_answers respectively
                  right_answers=convert(l_answer[j])
                  stude_answers=convert(s_answer[i])
                  ##function to compare individual words for i which has not been marked for every j which is right answer
                  def check_point(list1, list2):      
                        current_correct_answer=[]
                        #check student words for every lec words
                        def check_right(myList,x,y):
                              if x==y:
                                    ##add similar list to my list
                                    myList.append(x)
                                    #remove right answer from lecturer words
                                    right_answers.remove(x)
                        #actual implementation of check_right
                        for stude in stude_answers:
                              for right in right_answers:
                                    check_right(current_correct_answer,stude,right)
                        print(current_correct_answer)
                        similar_list_ratio.append(math.trunc(100*len(current_correct_answer)/len(right_answers)))
            if max(similar_list_ratio)>50:
                  result_points.append(1)
                  l_answer.remove(l_answer[similar_list_ratio.index(max(similar_list_ratio))])
      similar_list_ratio.clear()
      
compare(student_as, lec_as)
print(sum(result_points))
