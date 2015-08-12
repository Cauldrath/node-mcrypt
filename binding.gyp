{
    "targets": [
        {
            "target_name": "mcrypt",
            "sources": [
                "src/mcrypt.cc"
            ],
            "include_dirs": [
                "/usr/include/",
                "/usr/local/include",
                "/usr/local/Cellar/mcrypt/",
                "/opt/local/include/",
                "./libmcrypt",
                "<!(node -e \"require('nan')\")"
            ],
            "link_settings": {
                "libraries": [
                    "-l../libmcrypt_a",
                    "-L/opt/local/lib/ -L/usr/local/lib",
                ]
            }
        }
    ]
}
