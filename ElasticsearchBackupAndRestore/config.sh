#!/usr/bin/env bash

#                                                                 .   oooo
#                                                                .o8   `888
#  .oooo.   oooo oooo    ooo  .oooo.o     .oooo.   oooo  oooo  .o888oo  888 .oo.
# `P  )88b   `88. `88.  .8'  d88(  "8    `P  )88b  `888  `888    888    888P"Y88b
#  .oP"888    `88..]88..8'   `"Y88b.      .oP"888   888   888    888    888   888
# d8(  888     `888'`888'    o.  )88b    d8(  888   888   888    888 .  888   888
# `Y888""8o     `8'  `8'     8""888P'    `Y888""8o  `V88V"V8P'   "888" o888o o888o
export AWS_ACCESS_KEY=""
export AWS_SECRET_KEY=""

#            .oooo.                                       .o88o.  o8o
#          .dP""Y88b                                      888 `"  `"'
#  .oooo.o       ]8P'     .ooooo.   .ooooo.  ooo. .oo.   o888oo  oooo   .oooooooo
# d88(  "8     <88b.     d88' `"Y8 d88' `88b `888P"Y88b   888    `888  888' `88b
# `"Y88b.       `88b.    888       888   888  888   888   888     888  888   888
# o.  )88b o.   .88P     888   .o8 888   888  888   888   888     888  `88bod8P'
# 8""888P' `8bd88P'      `Y8bod8P' `Y8bod8P' o888o o888o o888o   o888o `8oooooo.
#                                                                      d"     YD
#                                                                      "Y88888P'
export AWS_BUCKET=""
export AWS_REGION=""

# .ooooo.   .oooo.o    oooo d8b  .ooooo.  oo.ooooo.   .ooooo.
# d88' `88b d88(  "8    `888""8P d88' `88b  888' `88b d88' `88b
# 888ooo888 `"Y88b.      888     888ooo888  888   888 888   888
# 888    .o o.  )88b     888     888    .o  888   888 888   888
# `Y8bod8P' 8""888P'    d888b    `Y8bod8P'  888bod8P' `Y8bod8P'
#                                           888
#                                          o888o
export S3_MAX_RETRIES="3"
export S3_BASE_PATH=""
export BACKUP_INDICES=""
export ES_BACKUP_REPOSITORY_NAME=""

#                       oooo                               .
#                       `888                             .o8
#  .ooooo.   .oooo.o     888 .oo.    .ooooo.   .oooo.o .o888oo
# d88' `88b d88(  "8     888P"Y88b  d88' `88b d88(  "8   888
# 888ooo888 `"Y88b.      888   888  888   888 `"Y88b.    888
# 888    .o o.  )88b     888   888  888   888 o.  )88b   888 .
# `Y8bod8P' 8""888P'    o888o o888o `Y8bod8P' 8""888P'   "888"
export ES_HOST=""
export ES_HOST_PROTOCOL=""
export ES_PORT=""
