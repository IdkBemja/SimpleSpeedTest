$(document).ready(function(){
    start_page()
    start_speedtest()
    start_speedtest_again()
    home_button()
});

function home_button(){
    $(".go-home").click(function(){
        start_page();
    })
}

function start_page(){
    $(".results-panel").hide();
    $(".waiting-panel").hide();
    $(".error-panel").hide();
    $(".start-panel").show();
};

function start_speedtest(){
    $('#start-speedtest-button').click(function(){
        $(".start-panel").hide();
        $(".waiting-panel").show();

        $.ajax({
            url: '/start-speedtest',
            type: 'GET',
            success: function(data){
                console.log(data);
                $(".waiting-panel").hide();
                updateResults(data)
                $(".results-panel").show();
            },
            error: function(error){
                $(".waiting-panel").hide();
                $(".error-panel").show();
                console.error('Error:', error);
            }
        });
    });
}
function start_speedtest_again(){
    $("#start-speedtest-button2").click(function(){
        $(".results-panel").hide();
        $(".start-panel").show();
    })
}

function updateResults(data) {

    var formattedDownloadSpeed = parseFloat(data.download_speed_mbps).toFixed(2);
    var formattedUploadSpeed = parseFloat(data.upload_speed_mbps).toFixed(2);
    var formattedping = Math.round(data.user_ping);

    // Update Download and updload results
    $('.download p').text(formattedDownloadSpeed);
    $('.upload p').text(formattedUploadSpeed);

    // Update the resume results
    $('.resume-results li:nth-child(1)').text(formattedping + ' ms');
    $('.resume-results li:nth-child(2)').html('<i class="bi bi-arrow-down-circle download_icon"></i> ' + formattedDownloadSpeed + ' Mbps');
    $('.resume-results li:nth-child(3)').html('<i class="bi bi-arrow-up-circle upload_icon"></i> ' + formattedUploadSpeed + ' Mbps');

    // Update the basic information

    // Server Side
    $('.server_info li:nth-child(1)').html('<i class="bi bi-globe2 color-gray"></i> ' + data.server_isp);
    $('.server_info li:nth-child(2)').text(data.server_name);


    // Client Side
    $('.user_info li:nth-child(1)').html('<i class="bi bi-person-circle color-gray"></i> ' + data.user_isp);
    $('.user_info li:nth-child(2)').text(data.user_ip);
}