# SPDX-FileCopyrightText: 2022 Kota Suzuki s21c1064cl@s.chibakoudai.jp
# SPDX-License Identifier: BSD-3-Claus

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    talker = launch_ros.actions.Node(
            package='mypkg',
            executable='talker',
            )
    listener = launch_ros.actions.Node(
            package='mypkg',
            executable='listener',
            output='screen'
            )

    return launch.LaunchDescription([talker, listener])

