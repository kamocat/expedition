import rclpy
from rclpy.node import Node
import numpy as np

from nav_msgs.msg import OccupancyGrid, Odometry, Path
from geometry_msgs.msg import *
from . import plan


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('expedition')
        self.pos = Point()
        self.sub = [
                self.create_subscription(
            OccupancyGrid,
            'map',
            self.create_path,
            1),
                self.create_subscription(
            Odometry,
            'odom',
            self.get_pos,
            1),
        ]

        self.pub = [
                self.create_publisher(
                    Path, 'plan', 10)
                ]
        # prevent unused variable warning
        self.pub
        self.sub 

    def create_path(self, msg):
        #FIXME: Account for map orientation
        x = self.pos.x - msg.info.origin.position.x
        y = self.pos.y - msg.info.origin.position.y
        k = 1 / msg.info.resolution
        map1 = np.asarray(msg.data).reshape((msg.info.width, msg.info.height))
        points = plan.plan(map1, int(x*k), int(y*k), 1)
        def toPose(a):
            b=PoseStamped()
            b.pose.position.x = a[0]*msg.info.resolution + msg.info.origin.position.x
            b.pose.position.y = a[1]*msg.info.resolution + msg.info.origin.position.y
            return b
        path = Path()
        path.header = msg.header
        path.poses = [toPose(x) for x in points]
        self.pub[0].publish(path)


    def get_pos(self, msg):
        self.pos = msg.pose.pose.position
        #self.get_logger().info(f'position: ({self.pos.x:0.3f},{self.pos.y:0.3f},{self.pos.z:0.3f})')


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
