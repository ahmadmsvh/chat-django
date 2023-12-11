from colors import Bcolors as C


def handle_session(request, response):

    try:
        counter = request.session.get('counter', 0) + 1
        names_list = request.session.get('names', "")

        name = request.GET["name"]

        if counter == 1:
            names_list = f"{name}"
        elif name not in ['number', 'list']:
            names_list = f"{names_list}, {name}"

        request.session['counter'] = counter
        request.session['names'] = names_list


        try:
            request_headers_cookie = request.headers['Cookie']
            print(C.GRLIGT, request_headers_cookie, C.ENDC)
            request_cookie = request.COOKIES
            print(C.BLLIGT, request_cookie, C.ENDC)
        except Exception as e:
            print(e)

        if request.session['counter'] < 5:
            response.set_cookie('cookie-testing', request.session['names'])
            response.headers['headers-testing'] = 'Ahmad-Mousavi'
            print(C.HEADER, request.session['counter'], "cookies", C.ENDC)
        else:
            print(C.GRLIGT, request.session['counter'], C.ENDC)
            del request.session['counter']
            del request.session['names']
            response.delete_cookie('cookie-testing')
            # del request.session['username']

        ret = {"request":request, "response":response}
        return ret

    except Exception as e:
        print(C.YLW, e, C.ENDC)
        print(C.FAIL, '--------- Session has expired ---------', C.ENDC)
        ret = {"request": request, "response": response}
        return ret


