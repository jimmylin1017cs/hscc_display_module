from flask import Flask, request


video_url = 'http://140.113.86.135:8090'
local_url = 'http://localhost:5000'

checkbox_name = 'person'
name_list = list()
enable_list = list()

selector_app = Flask(__name__)

def load_name_list():
    global name_list

    with open('tag.txt', 'r') as file:
        name_list = file.read().splitlines()

def load_enable_list():
    global enable_list

    with open('enable_tag.txt', 'r') as file:
        enable_list = file.read().splitlines()


@selector_app.route('/', methods=['GET', 'POST'])
def index():
    global enable_list

    load_name_list()

    if request.method == 'POST':
        enable_list = request.form.getlist(checkbox_name)
        print(enable_list)

        with open('enable_tag.txt', 'w') as file:
            for name in enable_list:
                file.write(name + '\n')


    s = '<form method="post">'

    for name in name_list:
        if( name in enable_list ):
            s += '<input type="checkbox" name="' + checkbox_name + '" value="' + name + '" style="width:20px; height:20px;" checked>' + '<span style="font-size:24px;">' + name + '</span>'
        else:
            s += '<input type="checkbox" name="' + checkbox_name + '" value="' + name + '" style="width:20px; height:20px;">' + '<span style="font-size:24px;">' + name + '</span>'
        
        s += '<br>'

    s += '<br><input type="submit" value="Submit" style="font-size:24px;"></form>'

    #s += '<div><embed src="' + video_url + '" style="width:800px; height: 600px;"></div>'
    #s += '<div><embed src="' + video_url + '" style="width: 1920px; height: 1080px;"></div>'

    return s

@selector_app.route('/demo', methods=['GET', 'POST'])
def display_web():
    #s = '<div><iframe src="' + local_url + '" style="width:1352px; height:200px;"></iframe></div>'
    #s += '<div><iframe src="' + video_url + '" style="width:1352px; height:1013px;"></iframe></div>'
    s = '<iframe src="' + video_url + '" style="width:1280px; height:720px;"></iframe>'
    s += '<iframe src="' + local_url + '" style="width:200px; height:720px;"></iframe>'
    #s = '<div><embed src="' + local_url + '" style="width: 1920px; height: 1080px;"></div>'
    #s += '<div><embed src="' + video_url + '" style="width: 1920px; height: 1080px;"></div>'

    return s

if __name__ == '__main__':
    selector_app.run()