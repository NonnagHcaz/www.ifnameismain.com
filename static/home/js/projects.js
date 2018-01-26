// Credit goes to Adam Pritchard for repo lookup script
// https://crypti.cc/

$(function(){
    $.getJSON('https://api.github.com/users/NonnagHcaz/repos?callback=?',function(repos,textStatus,jqXHR){
        var repoTemplate;
        if(textStatus!=='success'){
            $('#github-repos').text('Failed to load repos');}
        repos=repos.data;
        repos=repos.filter(
            function(elem){
                return!elem.fork&&!elem.private;});
        repos.sort(
            function(a,b){
                return a.pushed_at<b.pushed_at;});
        repoTemplate=$('#github-repo-template').html();
        $('#github-repos').empty();
        $.each(repos,function(){
            $('#github-repos').append(_.template(repoTemplate,this));});});
    // $.getJSON('https://api.github.com/users/NonnagHcaz/gists?callback=?',function(gists,textStatus,jqXHR){var gistTemplate;if(textStatus!=='success'){$('#github-gists').text('Failed to load gists');return;} gists=gists.data;gists=gists.filter(function(elem){return!elem.private;});gists.sort(function(a,b){return a.updated_at<b.updated_at;});gists=_.map(gists,function(gist){gist.GIST_NAME=_.keys(gist.files).sort()[0];return gist;});gistTemplate=$('#github-gist-template').html();$('#github-gists').empty();$.each(gists,function(){$('#github-gists').append(_.template(gistTemplate,this));});});
    // $.getJSON('https://api.bitbucket.org/1.0/users/NonnagHcaz?callback=?',function(repos,textStatus,jqXHR){var repoTemplate;if(textStatus!=='success'){$('#bitbucket-repos').text('Failed to load repos');return;} repos=repos.repositories;repos=repos.filter(function(elem){return!elem.is_fork&&!elem.is_private;});repos.sort(function(a,b){return a.last_updated<b.last_updated;});repoTemplate=$('#bitbucket-repo-template').html();$('#bitbucket-repos').empty();$.each(repos,function(){$('#bitbucket-repos').append(_.template(repoTemplate,this));});});
});
