// Credit goes to Adam Pritchard for repo lookup script
// Site: https://crypti.cc/projects/
// Repo: https://github.com/adam-p/adam-p.github.com/blob/master/projects/projects.js

$(function(){
  $.getJSON('https://api.github.com/users/NonnagHcaz/repos?callback=?', function(repos, textStatus, jqXHR) {
    var repoTemplate;

    if (textStatus !== 'success') {
      $('#github-repos').text('Failed to load repos');
      return;
    }

    repos = repos.data;

    repos = repos.filter(function(elem) {
      // Don't show forks of other projects or private repos.
      return !elem.fork && !elem.private;
    });

    repos.sort(function(a, b) {
      return a.pushed_at < b.pushed_at;
    });

    // Make sure to pull out the template before emptying the element.
    repoTemplate = $('#github-repo-template').html();

    // Remove the "Loading..." message
    $('#github-repos').empty();

    // Render the repos
    $.each(repos, function() {
      $('#github-repos').append(_.template(repoTemplate, this));
    });
  });
});
