
    var url = 'ws://' + window.location.host + '/ws/chat/room/' + '{{ course.id }}/';
    var chatSocket = new WebSocket(url);

    chatSocket.onmessage = function(e){
        var data = JSON.parse(e.data);
        var message = data.message;

        var $chat = $('#chat');
        $chat.append('<div class="message">' + message + '</div>');
        $chat.scrollTop($chat[0].scrollHeight);
    };

    chatSocket.onclose = function(e){
        console.error('Chat socket closed unexpectedly');
    };
    
    var $input = $('#chat-message-input');
    var $submit = $('#chat-message-submit');

    $submit.click(function() {
        var message = $input.val();
        if (message) {
            //send message in JSON format
            chatSocket.send(JSON.stingify({'message': message}));

            //clear input
            $input.val('');

            //return focus
            $input.focus();
        }
    });

    $input.focus();
    $input.keyup(function(e) {
        if (e.which === 13) {
            // submit with enter/return key
            $submit.click();
            }
    });
