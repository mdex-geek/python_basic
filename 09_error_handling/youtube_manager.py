import json 

Store_youtubeData_file = 'youtube.txt'

def load_data():
    try:
        with open(Store_youtubeData_file,'r')as file:
            test = json.load(file)   
            # print(type(test))
            return(test)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(Store_youtubeData_file,'w') as file :
        json.dump(videos,file)


def list_all_videos(videos):
    print('\n')
    print("*" *70)
    for index , video in enumerate(videos,start=1):
        print(f"{index}. {video['name'] } , Duration : {video['time']}")

def add_video(videos):
    name = input("Enter video name:")
    time = input("Enter video time:")
    videos.append({'name':name,"time":time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int  (input("enter the video number to update"))
    if 1<=index<=len(videos):
       video= input("Enter the new video name")
       time= input("Enter the new video time")
       videos[index-1] = {'name': video , 'time': time}
       save_data_helper(videos)
    else:
        print("invalid index selected")


def delete_video(videos):
    list_all_videos(videos)
    index = int  (input("enter the video number to delete "))
    if 1<=index<=len(videos):
       del(videos[index-1] )
       save_data_helper(videos)
    else:
        print("invalid video index selected")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose and option")
        print("1. List  all youtube videos: ")
        print("2. Add a youtube video : ")
        print("3. update a youtube video details : ")
        print("4. delete a youtube video: ")
        print("5. Exit the app: ")
        choice = input("enter your choice: ")
        # print(videos)

        match choice :
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print('invalid choice ')

if __name__ == "__main__" :
    main()






