# Script generated with Bloom
pkgdesc="ROS - Driver module between Aldebaran's NAOqiOS and ROS. It publishes all sensor and actuator data as well as basic diagnostic for battery, temperature. It subscribes also to RVIZ simple goal and cmd_vel for teleop."


pkgname='ros-kinetic-naoqi-driver'
pkgver='0.5.10_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'ros-kinetic-catkin'
'ros-kinetic-cv-bridge'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-transport'
'ros-kinetic-kdl-parser'
'ros-kinetic-naoqi-bridge-msgs>=0.0.4'
'ros-kinetic-naoqi-libqi'
'ros-kinetic-naoqi-libqicore'
'ros-kinetic-orocos-kdl'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-rosbag-storage'
'ros-kinetic-rosconsole'
'ros-kinetic-rosgraph-msgs'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf2-geometry-msgs'
'ros-kinetic-tf2-msgs'
'ros-kinetic-tf2-ros'
)

depends=('boost'
'ros-kinetic-cv-bridge'
'ros-kinetic-image-transport'
'ros-kinetic-kdl-parser'
'ros-kinetic-naoqi-bridge-msgs>=0.0.4'
'ros-kinetic-naoqi-libqi'
'ros-kinetic-naoqi-libqicore'
'ros-kinetic-orocos-kdl'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-rosbag-storage'
'ros-kinetic-rosconsole'
'ros-kinetic-tf2-ros'
)

conflicts=('ros-kinetic-nao-driver'
'ros-kinetic-naoqi-rosbridge'
)
replaces=()

_dir=naoqi_driver
source=()
md5sums=()

prepare() {
    cp -R $startdir/naoqi_driver $srcdir/naoqi_driver
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

