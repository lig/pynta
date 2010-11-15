from pynta import urls, domains


# define apps for urls on all domains
urls += (
    (r'^$', 'app_name1'),
)

# define some more urls for apps
urls += (
    (r'^other/$', 'app_name2'),
)
# define urls with method parameters
urls += (
    (r'^other1/(\d+)/$', 'app_name3'),
    (r'^other2/(?P<named_parameter>\w+)$', 'app_name4'),
)

# define apps for domains
domains += (
    # full domain name
    (r'^www.example.com$', 'app_name5'),
    # subdomain name
    (r'^subdomain\.', 'app_name6'),
)
