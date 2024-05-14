import sqlite3

con = sqlite3.connect('youtube_videos.db')

cursor = con.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')


def list_all_video():
    cursor.execute('SELECT * FROM videos')  # this will execute the command 
    for row in  cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    con.commit()

def update_video(videoID,new_name,time):
    cursor.execute('UPDATE videos SET name = ?,time =? WHERE id =?',(new_name,time,videoID))
    con.commit()

def delete_video(videoID):
    cursor.execute('DELETE FROM videos where id =?',(videoID,))
    con.commit()
    
def main():
    while True:
        print('\n Youtube manager app with DB')
        print('1. list videos')
        print('2. add videos')
        print('3.update videos')
        print('4.delete videos')
        print('5. exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            list_all_video()
          
        elif choice == '2':
            name = input("enter the video name: ")
            time = input("enter the video time: ")
            add_video(name,time)
        elif choice == '3':
            videoID =input ("enter ythe video id to update: ")
            name = input("enter the video name: ")
            time = input("enter the video time: ")
            update_video(videoID,name,time)
        elif choice == '4':
            videoID =input ("enter ythe video id to update: ")
            delete_video(videoID)
            
        elif choice == '5':
            break
        else:
            print('invalid choice')
    con.close()


if __name__ == '__main__':
    main()


