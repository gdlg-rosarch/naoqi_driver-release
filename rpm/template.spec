Name:           ros-jade-naoqi-driver
Version:        0.5.4
Release:        0%{?dist}
Summary:        ROS naoqi_driver package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-jade-cv-bridge
Requires:       ros-jade-image-transport
Requires:       ros-jade-kdl-parser
Requires:       ros-jade-naoqi-bridge-msgs >= 0.0.4
Requires:       ros-jade-naoqi-libqi
Requires:       ros-jade-naoqi-libqicore
Requires:       ros-jade-orocos-kdl
Requires:       ros-jade-robot-state-publisher
Requires:       ros-jade-rosbag-storage
Requires:       ros-jade-tf2-ros
BuildRequires:  boost-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-diagnostic-msgs
BuildRequires:  ros-jade-diagnostic-updater
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-kdl-parser
BuildRequires:  ros-jade-naoqi-bridge-msgs >= 0.0.4
BuildRequires:  ros-jade-naoqi-libqi
BuildRequires:  ros-jade-naoqi-libqicore
BuildRequires:  ros-jade-orocos-kdl
BuildRequires:  ros-jade-robot-state-publisher
BuildRequires:  ros-jade-rosbag-storage
BuildRequires:  ros-jade-rosgraph-msgs
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-tf2-geometry-msgs
BuildRequires:  ros-jade-tf2-msgs
BuildRequires:  ros-jade-tf2-ros
Conflicts:      ros-jade-nao-driver
Conflicts:      ros-jade-naoqi-rosbridge

%description
Driver module between Aldebaran's NAOqiOS and ROS. It publishes all sensor and
actuator data as well as basic diagnostic for battery, termperature. It
subscribes also to RVIZ simple goal and cmd_vel for teleop.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Aug 27 2015 Karsten Knese <karsten.knese@gmail.com> - 0.5.4-0
- Autogenerated by Bloom

* Wed Aug 26 2015 Karsten Knese <karsten.knese@gmail.com> - 0.5.3-0
- Autogenerated by Bloom

* Wed Aug 26 2015 Karsten Knese <karsten.knese@gmail.com> - 0.5.2-0
- Autogenerated by Bloom

* Tue Aug 11 2015 Karsten Knese <karsten.knese@gmail.com> - 0.5.1-0
- Autogenerated by Bloom

* Thu Jul 30 2015 Karsten Knese <karsten.knese@gmail.com> - 0.5.0-0
- Autogenerated by Bloom

