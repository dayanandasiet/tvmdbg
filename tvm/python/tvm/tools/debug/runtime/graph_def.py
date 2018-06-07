# coding: utf-8
# pylint: disable=fixme, too-few-public-methods, invalid-name
from __future__ import absolute_import as _abs


class GraphDef(object):
    def __init__(self, ctx, json_nodes):
        self._node = []
        for node in json_nodes['nodes']:
            self._node.append(Node(ctx, node))

    @property
    def node(self):
        return self._node


class Node(object):
    def __init__(self, ctx, node):

        name = node['name']
        op = node['op']
        device = "/job:localhost/replica:0/task:0/device:" + ctx  # TODO, remove job/replica/task
        input_lst = []
        attr = {}
        if 'inputs' in node:
            input_lst = node['inputs']
        if 'attrs' in node:
            attr = node['attrs']

        self._name = name
        self._op = op
        self._device = device
        self._input = input_lst
        self._attr = attr

    @property
    def device(self):
        return self._device

    @property
    def attr(self):
        return self._attr

    @property
    def name(self):
        return self._name

    @property
    def op(self):
        return self._op

    @property
    def input(self):
        return self._input
