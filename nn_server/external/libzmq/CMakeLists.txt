# libzmq version 4.3.4
set(DEP_LIBZMQ_VERSION "4.3.4")
set(DEP_LIBZMQ_LOC "https://github.com/zeromq/libzmq/releases/download/v4.3.4/zeromq-4.3.4.zip")

include(ExternalProject)

ExternalProject_Add(libzmq-build
    URL                 ${DEP_LIBZMQ_LOC}
    URL_HASH            SHA1=d639f350ef605c4d8f7710b19a6f2eb180790cfe
    CMAKE_ARGS          -G "Unix Makefiles"
                        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
                        -DCMAKE_C_FLAGS=-fPIC
                        -DCMAKE_BUILD_TYPE=Release
                        -DENABLE_TESTING=OFF
                        -DWITH_PERF_TOOL=OFF
                        -DZMQ_BUILD_TESTS=OFF
                        -DENABLE_CPACK=OFF
    BUILD_BYPRODUCTS    <INSTALL_DIR>/lib/libzmq.a
)

ExternalProject_Get_Property(libzmq-build INSTALL_DIR)

file(MAKE_DIRECTORY ${INSTALL_DIR}/include)

add_library(libzmq STATIC IMPORTED GLOBAL)
set_target_properties(libzmq
    PROPERTIES
        IMPORTED_LOCATION ${INSTALL_DIR}/lib/libzmq.a
        INTERFACE_INCLUDE_DIRECTORIES ${INSTALL_DIR}/include
        INSTALL_DIRECTORY ${INSTALL_DIR}
        VERSION ${DEP_LIBZMQ_VERSION}
)

add_dependencies(libzmq libzmq-build)
