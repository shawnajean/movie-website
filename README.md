# Movie Website Generator

This takes a movie list on TheMovieDB and turns it into a website. An example can be seen [here](https://shawnajean.github.io/movie-website/).

![](https://user-images.githubusercontent.com/775884/31321973-29707914-ac5c-11e7-9a39-d4e2866dc6ed.png)

## Prerequisites

This generator requires you to have an account, movie list, and API key at TheMovieDB.com. You can get an API key in [your TheMovieDB settings](https://www.themoviedb.org/settings/api). You can create a new movie list from [your account](https://www.themoviedb.org/list/new).

Once you have these set up, follow the steps below. You'll need your v3 API key and list ID [below]().

## Install

First, clone this repository:

`git clone https://github.com/shawnajean/movie-website.git`

Or download it using the green "Clone or download" button above and then clicking "Download ZIP".

Once you have the repository downloaded, you'll need to create a new file in the project directory. The file needs to be named `config.py` and include your API key and list ID with these variable names:

```
themoviedb_list_id = "XXXXX"
themoviedb_v3_api_key = "XXXXXXXXXXXXXXXXXXXXXXX"
```

To start, you can use my list ID `35496` as an example, but you will need your own API key.

Once the config file is set up, you can generate your site by running:

`python entertainment_center.py`

## Modifying the site

You can modify the styles and [title of the site(https://github.com/shawnajean/movie-website/blob/master/site_generator.py#L109) in the `site_generator.py` file.
