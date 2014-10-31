

import rpyc
from rpyc.utils.server import ThreadedServer
import logging
import deduplicator.dupCheck
import logSetup
import settings

import server.tree

#TODO: A much cleaner message-passing interface here would be quite nice

class DbInterfaceServer(rpyc.Service):

	def on_connect(self):
		print("Client Connection established!")

	def on_disconnect(self):
		print("Client Disconnected!")

	def exposed_loadTree(self, *args, **kwargs):
		print(server.tree.tree)
		server.tree.tree.loadTree(*args, **kwargs)

	def exposed_reloadTree(self, *args, **kwargs):
		print(server.tree.tree)
		server.tree.tree.reloadTree(*args, **kwargs)

	def exposed_nodeCount(self):
		return server.tree.tree.nodes


	class exposed_ArchChecker(deduplicator.dupCheck.ArchChecker):
		def exposed_isBinaryUnique(self, *args, **kwargs):
			return super().isBinaryUnique(*args, **kwargs)
		def exposed_isPhashUnique(self, *args, **kwargs):
			return super().isPhashUnique(*args, **kwargs)
		def exposed_getHashes(self, *args, **kwargs):
			return super().getHashes(*args, **kwargs)
		def exposed_deleteArch(self, *args, **kwargs):
			return super().deleteArch(*args, **kwargs)
		def exposed_addNewArch(self, *args, **kwargs):
			return super().addNewArch(*args, **kwargs)


	class exposed_TreeProcessor(deduplicator.dupCheck.TreeProcessor):
		def exposed_trimTree(self, *args, **kwargs):
			return super().trimTree(*args, **kwargs)

		def exposed_trimFiles(self, *args, **kwargs):
			return super().trimFiles(*args, **kwargs)

		def exposed_removeArchive(self, *args, **kwargs):
			return super().removeArchive(*args, **kwargs)


def run_server():
	print("Started.")
	serverLog = logging.getLogger("Main.RPyCServer")
	server = ThreadedServer(service=DbInterfaceServer, port = 12345, hostname='localhost', logger=serverLog)
	server.start()



def before_exit():
	print("Caught exit! Exiting")


import server_reloader

def main():
	logSetup.initLogging()

	server.tree.tree = deduplicator.dupCheck.TreeRoot(settings.PRELOAD_DIRECTORIES)

	print("Preloading cache directories")
	server.tree.tree.reloadTree()
	print("Loaded %s items" % server.tree.tree.nodeQuantity)
	# print("Testing reload")
	# server.tree.tree.reloadTree()
	# print("Starting RPC server")



	run_server()
	# server_reloader.main(
	# 	run_server,
	# 	before_reload=before_reload,
	# 	before_exit=before_exit
	# )

if __name__ == '__main__':
	main()