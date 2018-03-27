#J2T
import os

def genHtml():
    p = input("type folder p >> ")
    #convert path to windows path and vice versa###### to finish
    if p[0].isalpha():
        p2 = "/mnt/" + p[0].lower() + p[2:]
        p = p2.replace('\\', '/')
    if( p[-1] != '/'):
        p += '/'
    if (p[:5] == "/mnt/"):
        path = p[5].upper() + ":/" + p[7:]

    #check file type and add html accordingly
    video_formats = ["mp4", "jmepg"] #video formats to check for
    img_formats = ["jpg", "png", "gif"] #image formats to check for
    files_html = ""
    for files in os.walk(p):
        for file in files[2]:
            n = file.find('.') + 1
            if file[n:] in video_formats:
                files_html += '<li><video src="{}"></video></li>'.format(path+file)
                print(file[n:])
            elif file[n:] in img_formats:
                files_html += '<li><img src="{}"></img><li>'.format(path+file)


    html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <link rel="stylesheet" href="viewer.css">
            <title>File Viewer</title>
        </head>
        <body>
            <ul>
              {}
            </ul>
        </body>
        </html>
    """.format(files_html)
    f = open('htm.html', 'w')
    f.truncate()
    f.write(html)
    f.close()
    
def vDownloader(source):
    pass

