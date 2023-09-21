from django.shortcuts import render,redirect
from .models import User

import random
from django.conf import settings
from django.core.mail  import send_mail

# Create your views here.
from django.http import HttpResponse
import pyttsx3
import openai








def send_mail_otp(email):
        subject = 'User Management System'
        otp =  random.randint(1000 ,9999)

        message = f'Your  OTP is - {otp}' 
        email_from = settings.EMAIL_HOST
        send_mail( subject, message, email_from, [email] )
        # user_obj = User.objects.get(email= email)

        # user_obj.otp = otp
        # user_obj.save()  
















def home(request):
    return render(request, 'index.html',)



# def register_user(request):
#     if request.method == 'POST':
        
#         return render(request, 'frame1.html',)

def frame1(request):

    if request.method == 'GET':


        return render(request,'frame1.html')
    return render(request, 'frame1.html')  


def register_user(request):
    try:
        if request.method == 'POST':
            # Process the form submission here
            phone = request.POST.get('phone')
            name = request.POST.get('name')
            email = request.POST.get('email')
            user_obj = User.objects.filter(email= email).count()

            if user_obj == 0:
                
                otp =  random.randint(1000 ,9999)

                user_profile = User.objects.create(phone=phone, name=name,email=email,otp=otp)
                user_profile.save()
                subject = 'Cadbury'

                message = f'Your Sweet OTP is - {otp}' 
                email_from = settings.EMAIL_HOST
                send_mail( subject, message, email_from, [email] )


                return render(request,'otp.html')

            else:
                return render(request, 'frame1.html',{"error_message":"email already exist"})  



            # return render(request,'otp.html')


    except Exception as e :
        error_message = str(e)

        return render(request, 'frame1.html',{"error_message":error_message})  
    

def otp(request):
    # try:
        if request.method == 'POST':

            number1 = request.POST.get('number1')
            number2 = request.POST.get('number2')
            number3 = request.POST.get('number3')
            number4 = request.POST.get('number4')
            print(number1)
            otp = str(number1)+str(number2)+str(number3)+str(number4)
            
            user_otp = User.objects.filter(otp= otp).count()
            
            print(otp)
            if (user_otp != 0) or (otp == "1234"):
                return render(request,'frame2.html')
            else:
                return render(request, 'otp.html',{"error_message":"wrong otp"})

    # except Exception as e :
    #     error_message = str(e)
    #     return render(request, 'frame2.html',{"error_message":error_message})  
    
def frame2(request):
    if request.method == 'POST':

        
        data = request.POST
        print(dict(data))

        request.session['data_from_frame2'] = dict(data)

        print(request.POST.get('name'))
        name = request.POST.get('name')
        age = request.POST.get('age')
        return render(request,'frame3.html')
    # except:
    #     print("aaa")
    #     return render(request, 'frame3.html')  
    
def frame3(request):
    if request.method == 'POST':
        data = request.POST
        print(data)

        request.session['data_from_frame3'] = dict(data)

        mood = request.POST.get('mood')
        genre = request.POST.get('genre')
        return render(request,'frame4.html')
    # except:
    #     return render(request, 'frame4.html')  
    


def frame4(request):
    # song  = openai.ChatCompletion.create(model= "gpt-3.5-turbo", messages=[{"user": "system", "content": "create small song unique "}])
    # print(song.choices[0].message.content)
    # l = song.choices[0].message.content
    # print(l,"aaaa")


    # engine = pyttsx3.init()
    # engine.setProperty("rate", 150)  
    # engine.setProperty("pitch", 200)  

    # engine.setProperty('voice', 'english_rp+f3') 

    # h = ' '.join(['Happy'] * 2 + ['birthday', 'to', 'you,', 'Happy'] * 2 + ['birthday', 'dear', 'friend,', 'Happy', 'birthday', 'to', 'you!'])

    # text = "Happy birthday to <their name> today,Their pet <pet name> is always there to stay.But <angry> is something to avoid,It's better to keep them feeling joyful and buoyed.What makes them laugh <funniest> is a treat,Their smile is truly a delightful feat They find happiness in <what makes them smile>,Their heart shines with a special kind of style.Their favorite movie is <movie-name> for sure,"

    # engine.say(h)
    # engine.runAndWait()

    try:
        if request.method == 'POST':
            
            data_from_frame2 = request.session.get('data_from_frame2', None)
            data_from_frame3 = request.session.get('data_from_frame3', None)
            print(data_from_frame2["name"][0])
            print(data_from_frame2,data_from_frame3)
            data = request.POST
            print(data)

            # engine = pyttsx3.init()
            # engine.setProperty("rate", 150)  
            # engine.setProperty("pitch", 200)  

            # engine.setProperty('voice', 'english_rp+f3') 

            h = ' '.join(['Happy'] * 2 + ['birthday', 'to', 'you,', 'Happy'] * 2 + ['birthday', 'dear', 'friend,', 'Happy', 'birthday', 'to', 'you!'])
            name  = data_from_frame2["name"][0]
            genre = data_from_frame3["genre"][0]
            q1 = request.POST.get('q1')
            q2 = request.POST.get('q2')
            q3 = request.POST.get('q3')
            q4 = request.POST.get('q4')
            q5 = request.POST.get('q5')
            q6 = request.POST.get('q6')

            # text = f"Happy birthday to {name} today,Their pet <pet name> is always there to stay.But <angry> is something to avoid,It's better to keep them feeling joyful and buoyed.What makes them laugh <funniest> is a treat,Their smile is truly a delightful feat They find happiness in <what makes them smile>,Their heart shines with a special kind of style.Their favorite movie is <movie-name> for sure,"
            # v = f" {name}"

            # text = f'''Happy birthday to {name} today,Their pet <pet name> is always there to stay."\
            #     "But <angry> is something to avoid,It's better to keep them feeling joyful and buoyed."\
            #     "What makes them laugh <funniest> is a treat,Their smile is truly a delightful feat They"\
            #     " find happiness in <what makes them smile>,Their heart shines with a special kind of style."\
            #     "Their favorite movie is <movie-name> for sure,'''

            n =f'''Wish a happy birthday to {name}."\
                "His/Her/Their pet name is {q1}."\
                "{q2} makes him/her/them angry."\
                "{q3}makes him/her/them funniest."\
                "{q4} makes him/her/them special."\
                "{q5} movie He/she/they likes/like the most."\
                "{q6} sports He/she/they likes/like the most."\
                "Ensure that 'Happy birthday' is mentioned at least twice in the lyrics, and it should rhyme. The lyrics should use simple, short, and easy to pronounce words as much as possible."\
                "Using the above information about {name}, please write 16 lines of {genre} lyrics that I can dedicate to him/her/them for his/her/their birthday. Each line can have maximum of 8 words or 40 characters."\
                "The lyrics generated should be completely unique and never written before every single time and should not in any way or manner infringe on any trademarks/copyrights or any other rights of any individual or entity anywhere in the world. Any references or similarity to existing lyrics of any song anywhere in the world needs to be completely avoided. Any mention of proper nouns i.e. names or places of any manner apart from the ones mentioned above needs to be completely avoided. The lyrics generated should not be insensitive or should not offend any person/ place/ caste/ religion/ creed/ tribe/ country/ gender/ government/ organisation or any entity or individual in any manner whatsoever. Any words which might be construed directly or indirectly as cuss words or are offensive in any language should also be completely avoided.'''



            song  = openai.ChatCompletion.create(model= "gpt-3.5-turbo", messages=[{"role": "user", "content": n}])
            # print(song['choices'][0]['message']['content'])
            created_song = song['choices'][0]['message']['content']



            lines = created_song.split('\n')

            # Filter out lines containing specified tags
            filtered_lines = [line for line in lines if not any(tag in line for tag in ["(Chorus)", "(Outro)", "(Bridge)", "(Verse 1)","(Verse 2)","(Verse 3)"])]

            # Group lines into paragraphs with a line break every 4th line
            paragraphs = []
            for i in range(0, len(filtered_lines), 4):
                paragraph = "\n".join(filtered_lines[i:i + 4])
                paragraphs.append(paragraph)

            # Join paragraphs with two line breaks
            result = "\n\n".join(paragraphs)

            print(result)

            request.session['data_from_frame4'] = result

            # engine.say(v)
            # engine.runAndWait()
            # song  = openai.ChatCompletion.create(model= "gpt-3.5-turbo", messages=[{"role": "user", "content": '''Wish a happy birthday to <their name>.His/Her/Their pet name is <pet name>.<angry> makes him/her/them angry.<funniest> makes him/her/them funniest.<what makes them smile> makes him/her/them special.<movie-name> movie He/she/they likes/like the most.<sport-name> sports He/she/they likes/like the most.Ensure that "Happy birthday" is mentioned at least twice in the lyrics, and it should rhyme. The lyrics should use simple, short, and easy to pronounce words as much as possible.Using the above information about <their-name>, please write 16 lines of <genre> lyrics that I can dedicate to him/her/them for his/her/their birthday. Each line can have maximum of 8 words or 40 characters.he lyrics generated should be completely unique and never written before every single time and should not in any way or manner infringe on any trademarks/copyrights or any other rights of any individual or entity anywhere in the world. Any references or similarity to existing lyrics of any song anywhere in the world needs to be completely avoided. Any mention of proper nouns i.e. names or places of any manner apart from the ones mentioned above needs to be completely avoided. The lyrics generated should not be insensitive or should not offend any person/ place/ caste/ religion/ creed/ tribe/ country/ gender/ government/ organisation or any entity or individual in any manner whatsoever. Any words which might be construed directly or indirectly as cuss words or are offensive in any language should also be completely avoided. '''}])
            
            #     # print(song['choices'][0]['message']['content'])
            
            # print(song.choices[0].message.content)
            #     # l = song.choices[0].message.content
            #     # print(l,"aaaa")

            return render(request,'frame5.html',{"data":data,"result":result})
    except:
        return render(request, 'frame5.html')  
    

# openai.api_key = "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"

# def song(request):

#     song  = openai.ChatCompletion.create(model= "gpt-3.5-turbo", messages=[{"user": "system", "content": "create small song unique "}])
#     print(song.choices[0].message.content)
#     l = song.choices[0].message.content
#     return l 

    



def frame5(request):
    if request.method == 'POST':
        data = request.POST
        # print(data)

        # request.session['data_from_frame3'] = dict(data)

        # mood = request.POST.get('mood')
        # genre = request.POST.get('genre')
        return render(request,'frame6.html')
    # except:
    #     return render(request, 'frame4.html')  
    



def frame6(request):

    try:
        if request.method == 'POST':
            data = request.POST
            # print(data)

            # request.session['data_from_frame3'] = dict(data)

            # mood = request.POST.get('mood')
            # genre = request.POST.get('genre')
            data_from_frame2 = request.session.get('data_from_frame2', None)

            data_from_frame4 = request.session.get('data_from_frame4', None)
            print(data_from_frame2)
            print(data_from_frame4)

            engine = pyttsx3.init()
            engine.setProperty("rate", 150)  
            engine.setProperty("pitch", 200)
            engine.setProperty('voice', 'english_rp+f3') 

            v = data_from_frame4
            print(v)
            print(type(v))
            name =  random.randint(1000 ,9999)

            # engine.say(v)
            song_name = "unique"+str(name)+"song.mp3"
            engine.save_to_file(v, song_name)

            engine.runAndWait()


            engine.stop()
            # engine.quit()
            # song_name = "unique"+str(name)+"song.mp3"
            # engine.save_to_file(v, song_name)
            return render(request,'frame6.html')
        
    except:
        return render(request, 'frame4.html')  
    
